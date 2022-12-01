from django.urls import path
from Quiz import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("players/search", views.busqueda_futbolistas, name="Buscar Futbolista"),
    path("players/create", views.crear_futbolista, name='Crear Futbolista'),
    path("teams/create", views.crear_equipo, name='Crear Equipo'),
    path("country/create", views.crear_pais, name='Crear Pais'),
]
