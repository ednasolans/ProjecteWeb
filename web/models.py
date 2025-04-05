from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Ingredient (models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_amount = models.IntegerField()
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