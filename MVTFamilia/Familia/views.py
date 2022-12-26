from django.shortcuts import render
from Familia.models import Persona
from django.http import HttpResponse

# Create your views here.

def CrearFamilia(request):
    # BORRA TODA LA DATA
    todos_miembros = Persona.objects.all()
    todos_miembros.delete()

    # CARGA LA DATA
    miembro_1 = Persona.objects.create(tipo='PADRE', nombre='Vegeta', edad=59, sexoM = True, actividad='Principe', imagen='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzfx4XQgYNYb-uPj5TUxlX2a9tAYDgWsMzjg&usqp=CAU')
    miembro_2 = Persona.objects.create(tipo='MADRE', nombre='Bulma', edad=54, sexoM = False, actividad='Cientifica', imagen='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxOCmfbmh8YvtIQsTFFept3ZGeEC6MjRNM8A&usqp=CAU')
    miembro_3 = Persona.objects.create(tipo='HIJO', nombre='Trunks', edad=20, sexoM = True, actividad='Estudiante', imagen='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDc979hdmhJywEKFpixKLD0J2m4CpbbVWHpg&usqp=CAU')
    miembro_4 = Persona.objects.create(tipo='HIJA', nombre='Bra', edad=15, sexoM = False, actividad='Estudiante', imagen='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFAPZJWRKAALqk99F4xnJXS-3WJgIbSO07zg&usqp=CAU')

    return render(request,'crear_familia.html',context={})

def ListarFamilia(request):
    todos_miembros = Persona.objects.all()

    context = {
                'familia' : todos_miembros
              }
    return render(request,'listar_familia.html',context=context)