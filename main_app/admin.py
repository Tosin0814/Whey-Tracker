from django.contrib import admin
from .models import Whey, CustomerRating, Celebrity, Photo

# Register your models here.
admin.site.register(Whey)
admin.site.register(CustomerRating)
admin.site.register(Celebrity)
admin.site.register(Photo)