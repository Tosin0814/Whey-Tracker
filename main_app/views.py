from django.shortcuts import render
from .models import Whey


## Fake data used before model was created
# class Whey:
#     def __init__(self, name, protein_content, size, price, rating, review):
#         self.name = name
#         self.protein_content = protein_content
#         self.size = size
#         self.price = price
#         self.rating = rating
#         self.review = review

# whey = [
#     Whey('Sunshine Biopharma', 24, 5, 77, 4, 'Lean protein supplement with great taste and good values for money'),
#     Whey('Pure Protein Powder', 25, 5, 54, 4.5, 'Although the taste is not so great, it is very affordable and has a high protein content. It is difficult to find this product'),
#     Whey('Optimum Nutrition Gold Standard', 24, 5, 119, 3.8, 'High quality lean protein supplement used by athletes. It has a nice taste, but it is expensive compared to other brands on the market'),
# ]


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
    
    