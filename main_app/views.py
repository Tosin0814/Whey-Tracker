from nis import cat
from django.shortcuts import render, redirect
from .models import Whey, Celebrity
from .forms import CustomerRatingForm
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def whey_index(request):
#     whey = Whey.objects.all()
#     return render(request, 'whey/index.html', { 'whey': whey})

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
    
    
class WheyList(ListView):
    model = Whey
    template_name = 'whey/index.html'

class WheyCreate(CreateView):
    model = Whey
    fields = ['name','protein_content', 'size', 'price', 'rating', 'review']
    template_name = 'whey/create.html'

class WheyUpdate(UpdateView):
    model = Whey
    template_name = 'whey/create.html'
    fields = ['protein_content', 'size', 'price', 'rating', 'review']

class WheyDelete(DeleteView):
    model = Whey
    template_name = 'whey/confirm_delete.html'
    success_url = '/whey/'


def add_customer_review(request, whey_id):
    form = CustomerRatingForm(request.POST)
    if form.is_valid():
        new_customer_review = form.save(commit=False)
        new_customer_review.whey_id = whey_id
        new_customer_review.save()
    return redirect('whey_detail', whey_id = whey_id)


class CelebList(ListView):
    model = Celebrity
    template_name = 'celebrities/index.html'

class CelebDetail(DetailView):
    model = Celebrity
    template_name = 'celebrities/detail.html'

class CelebCreate(CreateView):
    model = Celebrity
    fields = ['name', 'profession']
    template_name = 'celebrities/create.html'

class CelebUpdate(UpdateView):
    model = Celebrity
    fields = ['profession']
    template_name = 'celebrities/create.html'

class CelebDelete(DeleteView):
    model = Celebrity
    template_name = 'celebrities/confirm_delete.html'
    success_url = '/celebrities/'


# Used for listing celebs to add instead of Select
# def assoc_celeb(request, whey_id, celebrity_id):
#     Whey.objects.get(id=whey_id).celebrities.add(celebrity_id)
#     return redirect('whey_detail', whey_id=whey_id)

# Used for selecting celebs instead of listing
def assoc_celeb(request, whey_id):
    celeb_id = request.POST.get('celebs_whey_doesnt_have')
    print(f"We got: {celeb_id}")
    Whey.objects.get(id=whey_id).celebrities.add(celeb_id)
    return redirect('whey_detail', whey_id=whey_id)

def disassoc_celeb(request, whey_id, celebrity_id):
  Whey.objects.get(id=whey_id).celebrities.remove(celebrity_id)
  return redirect('whey_detail', whey_id=whey_id)