from django.contrib import admin
from .models import Profile, Ingredient, Recipe

# Register your models here.

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(Recipe)