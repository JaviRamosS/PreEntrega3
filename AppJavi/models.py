from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length = 40)
    breed = models.CharField(max_length = 40)
    age = models.IntegerField()
    owner_name = models.CharField(max_length = 40)