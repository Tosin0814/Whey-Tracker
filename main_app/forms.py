from dataclasses import field
from django.forms import ModelForm
from .models import CustomerRating, Celebrity

class CustomerRatingForm(ModelForm):
  class Meta:
    model = CustomerRating
    fields = ['user_name','rating', 'value', 'review_text']

# class AddCelebrityForm(ModelForm):
#   class Meta:
#     model = Celebrity
#     fields = ['name']