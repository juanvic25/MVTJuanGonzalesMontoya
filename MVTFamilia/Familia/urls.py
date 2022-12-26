from django.urls import path
from Familia.views import CrearFamilia, ListarFamilia, LimpiarFamilia

urlpatterns = [
    path('crear-familia/',CrearFamilia),
    path('listar-familia/',ListarFamilia),
    path('borrar-familia/',LimpiarFamilia),
]
