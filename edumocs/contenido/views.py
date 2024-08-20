from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Cursos
from .forms import PreInscripcionForm  # Importa desde forms.py
from .models import PreInscripcion 
from django.shortcuts import render, redirect




# Create your views here.

def navbar(request):
    return render(request,'contenido/BaseNavBar.html')

def inicio(request):
    return render(request,'contenido/inicio.html')

def cursos(request):
    # Obtener todos los cursos de la base de datos
    cursos_list = Cursos.objects.all()
    # Pasar los cursos al contexto de la plantilla
    context = {
        'cursos': cursos_list
    }
    return render(request, 'contenido/cursos.html', context)

def curso_detalle(request, id):
    curso = get_object_or_404(Cursos, id=id)
    
    if request.method == 'POST':
        curso.inscritos += 1
        curso.save()
        return JsonResponse({'inscritos': curso.inscritos})
    return render(request, 'contenido/cursoDetalle1.html', {'curso': curso})

def detalles_cursos(request):
    return render(request,'contenido/detalles_cursos.html')

def acercade(request):
    return render(request,'contenido/acercade.html')



def foro(request):
    return render(request,'contenido/foro.html')


from django.shortcuts import render

def preguntas(request):
    return render(request, 'contenido/preguntas.html')

from django.shortcuts import render

def chat(request):
    # Provide data for the template, if needed
    context = {}
    return render(request, 'contenido/chat.html', context)



def cursos_view(request):
    cursos = Cursos.objects.all()
    return render(request, 'contenido/cursos.html', {'cursos': cursos})

def login(request):
    context={}
    return render(request, 'contenido/login.html', context)

def curso_detail(request, curso_id):
    curso = get_object_or_404(curso, id=curso_id)
    if request.method == 'POST':
        curso.inscritos += 1
        curso.save()
        return JsonResponse({'inscritos': curso.inscritos})
    return render(request, 'contenido/cursoDetalle1.html', {'curso': curso})

def PreInscripcion(request):
    if request.method == 'POST':
        form = PreInscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PreInscripcion')  # Redirige a una página de éxito o a cualquier otra vista
    else:
        form = PreInscripcionForm()

    return render(request, 'contenido/preInscripcion.html', {'form': form})


