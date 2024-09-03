from django.shortcuts import render  
from .models import Producto
from django.views.generic import ListView  
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy  

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import login, logout, authenticate  

def login_request(request):

    if request.method == "POST":  
        form = AuthenticationForm(request, data=request.POST)  
        print(form)  

        if form.is_valid():
            usuario = form.cleaned_data.get("username")  
            clave = form.cleaned_data.get("password")  

            nombre_usuario = authenticate(username=usuario, password=clave)  

            if nombre_usuario is not None:  
                login(request, nombre_usuario)  
                return render(request, 'plantillas/app/padre.html', {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  
            else:  
                form = AuthenticationForm()  
                return render(request, 'plantillas/users/login.html', {"mensaje":"Error, datos incorrectos", "form": form}) 
        else:  
            return render(request, 'plantillas/app/padre.html', {"mensaje":"Error, formulario inválido"}) 

    form = AuthenticationForm()  
    return render(request, 'plantillas/users/login.html', {"form":form})  



def about(request):
    return render(request, 'plantillas/app/about.html')


class ProductoListView(LoginRequiredMixin, ListView):
   
    model = Producto  
    template_name = 'plantillas/vistasclases/list.html' 


class ProductoDetalle(LoginRequiredMixin, DetailView):
  
    model = Producto
    template_name = 'plantillas/vistasclases/detalle.html' 


class ProductoCreateView(LoginRequiredMixin, CreateView):
   
    model = Producto
    template_name = 'plantillas/vistasclases/form.html' 
    success_url = reverse_lazy("List") 
    fields = ["categoria", "producto"]  

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
   
    model = Producto
    template_name = 'plantillas/vistasclases/edit.html'
    success_url = reverse_lazy("List")
    # success_url = 'plantillas/vistasclases/lista/' 
    fields = ["categoria", "producto"]

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
   
    model = Producto
    success_url = reverse_lazy("List")  
    template_name = 'plantillas/vistasclases/confirm_delete.html'