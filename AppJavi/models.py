from django.db import models
from django.views.generic import ListView

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length = 40)
    breed = models.CharField(max_length = 40)
    age = models.IntegerField()
    owner_name = models.CharField(max_length = 40)

    def __str__(self):
        return f"Name: {self.name} - Breed: {self.breed} - Age: {self.age}"

class DogList(ListView):
    model = Dog
    template_name = "AppJavi/dogs.html"

