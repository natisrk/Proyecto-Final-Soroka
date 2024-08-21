from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Cliente, Producto, Envio

# Create your views here.


def inicio(request):
    return render(request,'plantillas/app/padre.html')


def cliente(req):
    return render(req,'plantillas/app/cliente.html')

def producto(req):
    return render(req,'plantillas/app/producto.html')

def envio(req):
    return render(req,'plantillas/app/envio.html')


def clienteform(req):
    
    if req.method == 'POST':
    
     cliente = Cliente(nombre=req.POST['nombre'],apellido=req.POST['apellido'])
        
     cliente.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/clienteform.html')



def productoform(req):
    
    if req.method == 'POST':
    
     producto = Producto(categoria=req.POST['categoria'],producto=req.POST['producto'])
        
     producto.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/productoform.html')


def envioform(req):
    
    if req.method == 'POST':
    
     envio = Envio(calle=req.POST['calle'],numero=req.POST['numero'],localidad=req.POST['localidad'])
        
     envio.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/envioform.html')

