from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.

from django.shortcuts import render
from .models import Recipe
from .utils import get_recipe_from_api

def recipe_detail(request, recipe_id):
    recipe = get_recipe_from_api(recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

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
    return redirect('home')

