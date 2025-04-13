from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
import requests
from django.http import HttpResponseForbidden
from .models import Recipe
# Create your views here.

from django.shortcuts import render
from .models import Recipe, SavedRecipe
from .utils import get_recipe_from_api

# Vista per veure les receptes (NO ESTA COMPLETA NI ESTA FETA LA PLANTILLA HTML)
def recipe_detail(request, recipe_id):
    recipe = get_recipe_from_api(recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})

# Vista per a la pàgina de registre mitjançant un mètode POST utilitza el formulari
# del fitxer forms.py per guardar les dades de registre i redirigir a la vista de login
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Vista de login per poder autenticar-se
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista de logout. Aquesta vista y la de login ens la proporciona Django de moment
def user_logout(request):
    logout(request)
    return redirect('inici')

# vista que recupera les receptes que ha guardat l'usuari
def collection_view(request):
    if not request.user.is_authenticated:
        # Redirect or return a forbidden response
        return HttpResponseForbidden("You must be logged in to view this page.")

    # Assuming the user is authenticated, proceed with the query
    saved_recipes = SavedRecipe.objects.filter(user=request.user)

    # Add any other logic here and return the response
    return render(request, 'collection.html', {'saved_recipes': saved_recipes})

def home(request):
    query = request.GET.get('q')
    if query:
        receptes = Recipe.objects.filter(name__icontains=query)
    else:
        receptes = Recipe.objects.all()

    return render(request, 'home.html', {'receptes': receptes, 'query': query})

#per buscar les receptes amb la api
def buscar_receptes(request):
    query = request.GET.get('q', '')
    api_url = 'https://api.spoonacular.com/recipes/complexSearch'
    api_key = 'la_teva_clau_api'  # Aquí hauràs de posar la teva clau d'API

    if query:
        params = {
            'query': query,
            'apiKey': api_key,
            'number': 10,  # Nombre de resultats que vols obtenir
        }

        # Feu la petició a l'API
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            # Si la resposta és exitosa, obtenir les dades
            receptes_data = response.json()

            # Passar les receptes a la plantilla
            receptes = receptes_data.get('results', [])
            return render(request, 'recepies.html', {'receptes': receptes})

    # Si no es troben resultats, mostra una vista buida
    return render(request, 'recepies.html', {'receptes': []})