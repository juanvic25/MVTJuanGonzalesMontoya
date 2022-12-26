from django.urls import path
from Familia.views import CrearFamilia, ListarFamilia

urlpatterns = [
    path('crear-familia/',CrearFamilia),
    path('listar-familia/',ListarFamilia)
]
