from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Ingredient (models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_amount = models.IntegerField(max_length=10)
    unit_mesurement = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name