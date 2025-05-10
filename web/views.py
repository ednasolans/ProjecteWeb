from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
from django.conf import settings
from .forms import RecipeForm


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
@login_required
def collection_view(request):
    saved_recipes = SavedRecipe.objects.filter(user=request.user)
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

    results_per_page = 10

    if query:
        params = {
            'query': query,
            'apiKey': settings.SPOONACULAR_API_KEY,
            'number': results_per_page,  # Número de resultados por página
        }

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Lanza un error si la respuesta no es exitosa

            receptes_data = response.json()

            receptes = receptes_data.get('results', [])

            page_number = request.GET.get('page', 1)
            paginator = Paginator(receptes, results_per_page)

            try:
                page_obj = paginator.get_page(page_number)
            except EmptyPage:
                page_obj = paginator.get_page(paginator.num_pages)
            except PageNotAnInteger:
                page_obj = paginator.get_page(1)

            return render(request, 'recipes.html', {'page_obj': page_obj, 'query': query})

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            return render(request, 'recipes.html', {'error': 'Error al obtener recetas de la API.'})

    return render(request, 'recipes.html', {'receptes': [], 'query': query})


def veure_detall_recepta(request, recipe_id):
    recipe = get_recipe_from_api(recipe_id, request.user)
    if not recipe:
        return render(request, 'error.html', {'message': 'No s\'ha pogut carregar la recepta.'})

    return render(request, 'recipe_detail.html', {'recipe': recipe})


@login_required
def guardar_recepta(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    saved, created = SavedRecipe.objects.get_or_create(user=request.user, recipe=recipe)

    if created:
        print("Recepta guardada correctament.")
    else:
        print("Aquesta recepta ja està guardada.")

    return redirect('collection')


@login_required
def crear_recepta(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user  # vinculem la recepta amb l'usuari actual
            recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

@login_required
def editar_recepta(request, pk):
    recepta = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recepta)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recepta.pk)
    else:
        form = RecipeForm(instance=recepta)

    return render(request, 'web/editar_recepta.html', {'form': form})

@login_required
def eliminar_recepta_guardada(request, recipe_id):
    # Obtenim la recepta guardada per l'usuari
    saved_recipe = get_object_or_404(SavedRecipe, user=request.user, recipe_id=recipe_id)

    # Eliminem la recepta guardada
    saved_recipe.delete()

    # Redirigim l'usuari a la vista de la col·lecció de receptes guardades
    return redirect('collection')


