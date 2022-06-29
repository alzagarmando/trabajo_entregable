from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.http  import HttpResponse
from django.template import Template,Context
import datetime 
from ejemploLucaApp.models import Curso
# Create your views here.
 
def inicio(request):
    nombre='lucas'
    hoy=datetime.datetime.now()  
    notas=[2,3,10,6,4,5]
    
   
    return render(request,"index.html",{"mi_nombre":nombre,"dia_hoy":hoy,"notas":notas})

def crear_curso(request):
        nombre="pyhon"
        comision=31000
        nuevo_curso=Curso(nombre=nombre,comision=comision)
        nuevo_curso.save()
        return HttpResponse(f"hemos agrgado el curso{nombre} con comicion {comision}")

 
