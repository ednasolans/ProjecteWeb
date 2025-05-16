import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

import django
django.setup()

import subprocess
from django.contrib.auth.models import User

from web.models import Recipe, SavedRecipe

# Elimina los datos existentes (opcional)
print("🧹 Limpiando base de datos...")
User.objects.exclude(is_superuser=True).delete()
Recipe.objects.all().delete()
SavedRecipe.objects.all().delete()

# Crea usuarios de prueba
print("👤 Creando usuario de prueba...")
user, created = User.objects.get_or_create(username='user1', email='user1@example.com')
if created:
    user.set_password('testpass123')
    user.save()

# Ejecuta los tests de Behave
print("🚀 Ejecutando Behave...")
subprocess.run(['behave'])

print("✅ Tests finalizados.")
