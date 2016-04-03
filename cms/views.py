from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
# Create your views here.

def mostrar (request, key):
    try:
        valor = Pages.objects.get(id=key)
        respuesta = "El valor es " + valor.page
    except Pages.DoesNotExist:
        respuesta = "Esta clave no existe"
    return HttpResponse(respuesta)
def add(request, key, valor):
    nuevo = Pages(name=key,page=valor)
    nuevo.save()
    return HttpResponse("Nuevo elemento almacenado")
def listar(request):
    listado = Pages.objects.all()
    respuesta = "<ol>"
    for elemento in listado:
        respuesta += "<li>" + "key: " + str(elemento.id)
        respuesta += " name: " + str(elemento.name)
    respuesta += "</ol>"
    return HttpResponse(respuesta)
def notFound(request):
    return HttpResponse("Not Found: Argumentos invalidos")
