from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Cliente, Producto, Envio
from django.contrib.auth.decorators import login_required
from datetime import datetime



# Create your views here.


def inicio(request):
    hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'plantillas/app/padre.html', {'hoy': hoy})

def about(request):
    return render(request,'plantillas/app/about.html')


@login_required
def cliente(req):
    
    if req.method == 'POST':
    
     cliente = Cliente(nombre=req.POST['nombre'],apellido=req.POST['apellido'])
        
     cliente.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/cliente.html')


@login_required
def producto(req):
    
    if req.method == 'POST':
    
     producto = Producto(categoria=req.POST['categoria'],producto=req.POST['producto'])
        
     producto.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/producto.html')


@login_required
def envio(req):
    
    if req.method == 'POST':
    
     envio = Envio(calle=req.POST['calle'],numero=req.POST['numero'],localidad=req.POST['localidad'])
        
     envio.save()
        
     return render(req,'plantillas/app/padre.html')
    
    return render(req,'plantillas/app/envio.html')


def busquedanombre(req):
    return render(req,'plantillas/app/busquedanombre.html')

def buscar(req):

    if req.GET["nombre"]:
    
        nombre = req.GET['nombre']

        clientes = Cliente.objects.filter(nombre__icontains=nombre)

        return render(req, "plantillas/app/resultadobusqueda.html", {"clientes": cliente, "nombre":nombre})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

@login_required
def leerclientes(request):

      cliente = Cliente.objects.all()

      contexto= {"cliente":cliente} 

      return render(request, 'plantillas/app/leerclientes.html',contexto)

@login_required
def eliminarcliente(request, cliente_nombre):
 
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()
 
    cliente = Cliente.objects.all()  
 
    contexto = {"cliente": cliente}
 
    return render(request, 'plantillas/app/leerclientes.html', contexto)


def ClienteFormulario(request):  

    print("Entrando en la vista clienteformulario")  

    if request.method == 'POST':
        print("Solicitud POST recibida")  

        miFormulario = ClienteFormulario(request.POST) 

        if miFormulario.is_valid():
            print("Formulario válido")  
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'])
           
            cliente.save()

            return render(request, 'plantillas/app/padre.html') 
        else:
            print("Formulario no válido") 

    else:
        print("Solicitud GET recibida") 
        miFormulario = ClienteFormulario()

    return render(request, 'plantillas/app/cliente.html', {"miFormulario": miFormulario})

