from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hoja
from .forms import HojaForm 
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def hojas(request):
    hojas=Hoja.objects.all()
    #print(hojas)
    #return render(request, 'hojas/index.html')
    return render(request, 'hojas/index.html',{'hojas':hojas})#la varible verde es la que se esta pasando al for en index
         
def crearh(request):
    formulario=HojaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('hojas')
    return render(request, 'hojas/crearh.html',{'formulario':formulario})

def editarh(request,id):
    hoja=Hoja.objects.get(id=id)
    formulario=HojaForm(request.POST or None, request.FILES or None, instance=hoja)
    if formulario.is_valid() and request.POST: #o request.POST
        formulario.save()
        return redirect('hojas')
    return render(request, 'hojas/editarh.html',{'formulario':formulario})

def eliminarh(request, id):
    hoja=Hoja.objects.get(id=id)
    hoja.delete()
    return redirect('hojas')