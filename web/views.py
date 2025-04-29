from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
import requests
from django.http import HttpResponseForbidden
from .models import Recipe, SavedRecipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_recipe_from_api

# Create your views here.

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
            form.save_profile()  # <-- Cambia aquí
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

# Vista de logout.
def user_logout(request):
    logout(request)
    return redirect('home')

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

def buscar_receptes(request):
    query = request.GET.get('q', '')
    api_url = 'https://api.spoonacular.com/recipes/complexSearch'
    api_key = '7d703462d2f842c987df625bab42b119'  # Aquí debes poner tu clave de API

    # Definir la cantidad de resultados por página
    results_per_page = 10

    if query:
        params = {
            'query': query,
            'apiKey': api_key,
            'number': results_per_page,  # Número de resultados por página
        }

        try:
            # Realizar la solicitud a la API
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Lanza un error si la respuesta no es exitosa

            # Si la respuesta es exitosa, obtener los datos
            receptes_data = response.json()

            # Extraer las recetas
            receptes = receptes_data.get('results', [])

            # Para la paginación, usar los resultados y la página actual
            page_number = request.GET.get('page', 1)
            paginator = Paginator(receptes, results_per_page)

            try:
                page_obj = paginator.get_page(page_number)
            except EmptyPage:
                page_obj = paginator.get_page(paginator.num_pages)
            except PageNotAnInteger:
                page_obj = paginator.get_page(1)

            return render(request, 'recepies.html', {'page_obj': page_obj, 'query': query})

        except requests.exceptions.RequestException as e:
            # En caso de error con la solicitud, muestra un mensaje de error
            print(f"Error al obtener datos de la API: {e}")
            return render(request, 'recepies.html', {'error': 'Error al obtener recetas de la API.'})

    # Si no hay término de búsqueda, o si no se encuentran resultados, mostramos una vista sin resultados
    return render(request, 'recepies.html', {'receptes': [], 'query': query})

def guardar_recepta(request):
    query = request.GET.get('q', '')
