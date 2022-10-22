from django.shortcuts import render, redirect
from .models import Whey, Celebrity, Photo
from .forms import CustomerRatingForm
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = 'https://s3-ca-central-1.amazonaws.com/'
BUCKET = 'whey-tracker'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('whey_index')
        else:
            error_message = 'Invalid sign up - try again'
    # For a bad POST or a GET request, render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def whey_index(request):
#     whey = Whey.objects.all()
#     return render(request, 'whey/index.html', { 'whey': whey})

@login_required
def whey_detail(request, whey_id):
    whey = Whey.objects.get(id=whey_id)
    customer_rating_form = CustomerRatingForm()
    celebs_whey_doesnt_have = Celebrity.objects.exclude(id__in = whey.celebrities.all().values_list('id'))
    return render(request, 'whey/detail.html', {
        'whey': whey,
        'customer_rating_form': customer_rating_form,
        'celebs_whey_doesnt_have': celebs_whey_doesnt_have,
        }
    )
    
class WheyList(LoginRequiredMixin, ListView):
    model = Whey
    template_name = 'whey/index.html'

    ## If I want logged in user to view only their whey posts
    # def get_queryset(self):
    #     return Whey.objects.filter(user=self.request.user)

class WheyCreate(LoginRequiredMixin, CreateView):
    model = Whey
    fields = ['name','protein_content', 'size', 'price', 'rating', 'review']
    template_name = 'whey/create.html'
    # This inherited method is called when a valid whey form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the whey
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class WheyUpdate(LoginRequiredMixin, UpdateView):
    model = Whey
    template_name = 'whey/create.html'
    fields = ['protein_content', 'size', 'price', 'rating', 'review']

class WheyDelete(LoginRequiredMixin, DeleteView):
    model = Whey
    template_name = 'whey/confirm_delete.html'
    success_url = '/whey/'

@login_required
def add_customer_review(request, whey_id):
    form = CustomerRatingForm(request.POST)
    if form.is_valid():
        new_customer_review = form.save(commit=False)
        new_customer_review.user_name = request.user.username
        new_customer_review.whey_id = whey_id
        new_customer_review.save()
    return redirect('whey_detail', whey_id = whey_id)

class CelebList(LoginRequiredMixin, ListView):
    model = Celebrity
    template_name = 'celebrities/index.html'

class CelebDetail(LoginRequiredMixin, DetailView):
    model = Celebrity
    template_name = 'celebrities/detail.html'

class CelebCreate(LoginRequiredMixin, CreateView):
    model = Celebrity
    fields = ['name', 'profession']
    template_name = 'celebrities/create.html'

class CelebUpdate(LoginRequiredMixin, UpdateView):
    model = Celebrity
    fields = ['profession']
    template_name = 'celebrities/create.html'

class CelebDelete(LoginRequiredMixin, DeleteView):
    model = Celebrity
    template_name = 'celebrities/confirm_delete.html'
    success_url = '/celebrities/'


# Used for listing celebs to add instead of Select
# def assoc_celeb(request, whey_id, celebrity_id):
#     Whey.objects.get(id=whey_id).celebrities.add(celebrity_id)
#     return redirect('whey_detail', whey_id=whey_id)

# Used for selecting celebs instead of listing
@login_required
def assoc_celeb(request, whey_id):
    celeb_id = request.POST.get('celebs_whey_doesnt_have')
    print(f"We got: {celeb_id}")
    Whey.objects.get(id=whey_id).celebrities.add(celeb_id)
    return redirect('whey_detail', whey_id=whey_id)

@login_required
def disassoc_celeb(request, whey_id, celebrity_id):
  Whey.objects.get(id=whey_id).celebrities.remove(celebrity_id)
  return redirect('whey_detail', whey_id=whey_id)


@login_required
def add_photo(request, whey_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        # First delete previous photo (Only one photo is allowed)
        Photo.objects.get(whey_id=whey_id).delete()
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to whey_id or whey (if you have a whey object)
            photo = Photo(url=url, whey_id=whey_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('whey_detail', whey_id=whey_id)