from nis import cat
from django.shortcuts import render, redirect
from .models import Whey
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
    return render(request, 'whey/detail.html', {
        'whey': whey,
        'customer_rating_form': customer_rating_form
        }
    )
    
    
class WheyList(ListView):
    model = Whey
    template_name = 'whey/index.html'

# class WheyDetail(DetailView):
#     model = Whey
#     template_name = 'whey/detail.html'


class WheyCreate(CreateView):
    model = Whey
    fields = '__all__'
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
    return redirect('detail', whey_id = whey_id)
