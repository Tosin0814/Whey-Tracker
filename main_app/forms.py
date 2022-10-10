from django.forms import ModelForm
from .models import CustomerRating

class CustomerRatingForm(ModelForm):
  class Meta:
    model = CustomerRating
    fields = ['date', 'meal']