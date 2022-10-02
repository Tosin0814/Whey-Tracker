from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, DecimalValidator

# Create your models here.
class Whey(models.Model):
    name = models.CharField(max_length=300)
    protein_content = models.FloatField(validators=[MinValueValidator(0.0), DecimalValidator(5, 1)],)
    size = models.FloatField(validators=[MinValueValidator(1.0), DecimalValidator(5, 1)],)
    price = models.FloatField(validators=[MinValueValidator(0.0), DecimalValidator(5, 2)],)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0), DecimalValidator(5, 1)],)
    review = models.TextField(max_length=500)