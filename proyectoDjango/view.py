from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def hola(request):
    return HttpResponse("<h1>Hola buenas..¿Vienes al evento?</h1>")

def fecha(request):
    fecha=datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha}')

def calcular_fecha_nacimiento(request,edad):
    fecha_nacimiento=datetime.now().year-edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha_nacimiento}')

def mi_template(request):
    cargar_file= open(r'D:\Coder\proyectoDjango\templates\template.html','r')
    
    template= Template(cargar_file.read()) 
    cargar_file.close()

    template_renderizado=template

    return HttpResponse (template_renderizado)