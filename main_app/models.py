from django.db import models
from django.urls import reverse
from datetime import datetime  
from django.core.validators import MaxValueValidator, MinValueValidator, DecimalValidator


REVIEWS = (
    ('E', 'Excellent'),
    ('VG', 'Very Good'),
    ('G', 'Good'),
    ('A', 'Average'),
    ('B', 'Bad'),
    ('VB', 'Very Bad'),
    ('S', 'Stay Away')
)

PROFESSIONS = (
    ('M', 'Musician'),
    ('A', 'Actor'),
    ('S', 'Athlete'),
    ('O', 'Other'),
)
# Create your models here.
class Celebrity(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(
        max_length=2,
        choices = PROFESSIONS,
    )

    def __str__(self):
        return f"{self.name} the {self.get_profession_display()}"

    # Add this method to aid with Create Redirect to the new item page
    def get_absolute_url(self):
        return reverse('celeb_detail', kwargs={'pk': self.id})

    # change the default sort
    class Meta:
        ordering = ['name']


class Whey(models.Model):
    name = models.CharField(max_length=300)
    protein_content = models.FloatField(validators=[MinValueValidator(0.0)],)
    size = models.FloatField(validators=[MinValueValidator(1.0)],)
    price = models.FloatField(validators=[MinValueValidator(0.0)],)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    review = models.TextField(max_length=500)
    celebrities = models.ManyToManyField(Celebrity)

    def __str__(self):
        return self.name
    
    # Add this method to aid with Create Redirect to the new item page
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


class CustomerRating(models.Model):
    user_name = models.CharField(max_length=100)
    date = models.DateField('Rating Date', default=datetime.now)
    rating = models.FloatField(validators=[MinValueValidator(0.0)])
    value = models.CharField(
        max_length=2,
        choices=REVIEWS,
        )
    review_text = models.TextField(max_length=500)
    whey = models.ForeignKey(Whey, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_value_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']