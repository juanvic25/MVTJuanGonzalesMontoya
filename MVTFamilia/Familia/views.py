from django.shortcuts import render
from Familia.models import Persona
from django.http import HttpResponse

# Create your views here.

def CrearFamilia(request):
    miembro_1 = Persona.objects.create(tipo='Padre', nombre='Juan Gonzales Aspe', edad=59, sexoM = True, actividad='Empleado')
    miembro_2 = Persona.objects.create(tipo='Madre', nombre='Maria Montoya Cabrera', edad=54, sexoM = False, actividad='Ama de Casa')
    miembro_3 = Persona.objects.create(tipo='Hijo', nombre='Juan Gonzales Montoya', edad=30, sexoM = True, actividad='Empleado')
    miembro_4 = Persona.objects.create(tipo='Hijo', nombre='Sofia Gonzales Montoya', edad=24, sexoM = False, actividad='Estudiante')

    return render(request,'crear_familia.html',context={})

def ListarFamilia(request):
    todos_miembros = Persona.objects.all()

    context = {
                'familia' : todos_miembros
              }
    return render(request,'listar_familia.html',context=context)

def LimpiarFamilia(request):
    todos_miembros = Persona.objects.all()
    todos_miembros.delete()

    return HttpResponse('Se Borro toda la Familia')