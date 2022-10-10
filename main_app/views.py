from nis import cat
from django.shortcuts import render
from .models import Whey
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def whey_index(request):
    whey = Whey.objects.all()
    return render(request, 'whey/index.html', { 'whey': whey})

def whey_detail(request, whey_id):
    whey = Whey.objects.get(id=whey_id)
    return render(request, 'whey/detail.html', {'whey': whey})
    
    
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