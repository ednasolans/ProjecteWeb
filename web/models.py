from django.db import models

# Create your models here.

class Ingredients (models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_amount = models.IntegerField(max_length=10)
    unit_mesurement = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name
