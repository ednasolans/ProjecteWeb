from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Recipe
from .utils import get_recipe_from_api

def recipe_detail(request, recipe_id):
    recipe = get_recipe_from_api(recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
