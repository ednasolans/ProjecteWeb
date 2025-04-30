import requests
from .models import Recipe, Ingredient
from django.conf import settings

def get_recipe_from_api(recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    if recipe:
        return recipe

    api_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {'apiKey': settings.SPOONACULAR_API_KEY}  # <-- Usa aquí tu API KEY
    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    # Crear receta si todo está correcto
    recipe = Recipe.objects.create(
        id=recipe_id,
        name=data['title'],
        description=data.get('summary', ''),
        instructions=data.get('instructions', ''),
        image_url=data.get('image', None),
    )

    for ingredient_data in data.get('extendedIngredients', []):
        ingredient, created = Ingredient.objects.get_or_create(
            ingredient_name=ingredient_data['name'],
            defaults={
                'ingredient_amount': 0,
                'unit_mesurement': '',
            }
        )
        recipe.ingredients.add(ingredient)

    return recipe

