from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('collection/', views.collection_view, name='collection'),
    path('search/', views.buscar_receptes, name='buscar_receptes'),
    #no funciona encara lo de guardar receptes
    #path('guardar/<int:recipe_id>/', views.guardar_recepta, name='guardar_recepta'),
]
