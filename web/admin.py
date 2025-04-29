from django.contrib import admin
from .models import Profile, Ingredient, Recipe, SavedRecipe

# Register your models here.

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(SavedRecipe)
