from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render(request,'app/inicio.html')

def cliente(req):
    return render(req,'app/cliente.html')

def producto(req):
    return HttpResponse('vista producto')

def envio(req):
    return HttpResponse('vista envio')


