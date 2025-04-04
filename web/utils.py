import requests
from .models import Recipe, Ingredient

def get_recipe_from_api(recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    if recipe:
        return recipe

    api_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {'apiKey': 'tu_api_key'}
    response = requests.get(api_url, params=params)
    data = response.json()

    recipe = Recipe.objects.create(
        id=recipe_id,
        title=data['title'],
        description=data.get('summary', ''),
    )

    for ingredient_data in data['extendedIngredients']:
        ingredient, created = Ingredient.objects.get_or_create(
            name=ingredient_data['name']
        )
        recipe.ingredients.add(ingredient)

    return recipe
