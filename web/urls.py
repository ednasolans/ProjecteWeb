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
    path('recepta/<int:recipe_id>/', views.veure_detall_recepta, name='recipe_detail'),
    path('guardar_recepta/<int:recipe_id>/', views.guardar_recepta, name='store_recipe'),
    path('crear-recepta/', views.crear_recepta, name='crear_recepta'),
    path('recepta/<int:pk>/editar/', views.editar_recepta, name='editar_recepta'),
    path('eliminar_recepta_guardada/<int:recipe_id>/', views.eliminar_recepta_guardada,
         name='eliminar_recepta_guardada'),
]
