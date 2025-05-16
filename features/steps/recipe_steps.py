import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjecteWeb.settings')
django.setup()

from behave import given, when, then
from django.contrib.auth.models import User
from web.models import Recipe, SavedRecipe
from time import sleep

@given('estoy logueado como "{username}" con la contraseña "{password}"')
def step_impl(context, username, password):
    user, created = User.objects.get_or_create(username=username, email=f"{username}@example.com")
    if created:
        user.set_password(password)
        user.save()

    context.browser.visit(f'{context.base_url}/login/')
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    context.browser.find_by_value('Entrar').click()
    sleep(1)

@when('creo una receta llamada "{title}" con la descripción "{description}"')
def step_impl(context, title, description):
    browser = context.browser
    browser.visit(f'{context.base_url}/crear-recepta/')
    browser.fill('name', title)
    browser.fill('description', description)
    checkbox = context.browser.find_by_name('ingredients')
    checkbox[0].check()
    checkbox[1].check()
    browser.fill('instructions', 'Bate los huevos. Fríe las patatas. Junta todo.')
    browser.find_by_value('Guardar').click()
    sleep(1)

@then('debería ver la receta con título "{title}"')
def step_impl(context, title):
    assert title in context.browser.html

@given('ya tengo una receta llamada "{title}"')
def step_impl(context, title):
    user = User.objects.get(username='user1')
    Recipe.objects.get_or_create(name=title, created_by=user, defaults={
        'description': 'Descripción',
        'instructions': 'Instrucciones',
    })

@when('cambio el título a "{new_title}"')
def step_impl(context, new_title):
    user = User.objects.get(username='user1')
    recipe = Recipe.objects.filter(name='Tortilla', created_by=user).first()
    context.browser.visit(f'{context.base_url}/recepta/{recipe.pk}/editar/')
    context.browser.fill('name', new_title)
    context.browser.find_by_value('Guardar').click()
    sleep(1)

@given('tengo guardada una receta llamada "{title}"')
def step_impl(context, title):
    user = User.objects.get(username='user1')
    recipe, _ = Recipe.objects.get_or_create(name=title, created_by=user)
    SavedRecipe.objects.get_or_create(user=user, recipe=recipe)

@when('elimino la receta guardada')
def step_impl(context):
    user = User.objects.get(username='user1')
    recipe = Recipe.objects.filter(name='Tortilla Española', created_by=user).first()
    context.browser.visit(f'{context.base_url}/eliminar_recepta_guardada/{recipe.pk}/')
    sleep(1)

@then('no debería ver "{title}" en mi colección')
def step_impl(context, title):
    context.browser.visit(f'{context.base_url}/collection/')
    assert title not in context.browser.html
