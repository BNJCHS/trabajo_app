# administracion/urls.py

from django.urls import path
from . import views  # importa tus vistas

urlpatterns = [
    # Ruta de ejemplo
    path('', views.inicio, name='inicio'),
]
