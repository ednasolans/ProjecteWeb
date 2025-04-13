from django.urls import path
from . import views

urlpatterns = [
    path('', views.inici, name='inici'),  # Aquesta és la pàgina d'inici
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('colleccio/', views.collection_view, name='collection'),
    path('buscar/', views.buscar_receptes, name='buscar_receptes'),
]
