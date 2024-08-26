"""
URL configuration for entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from entrega.views import saludo, probando_template, agregar_cliente, agregar_producto, agregar_envio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
    path('saludo/', saludo),
    path('plantilla/', probando_template),
    path('agregar_cliente/<nom>/<ap>/', agregar_cliente),
    path('agregar_producto/<cat>/<prod>/', agregar_producto),
    path('agregar_envio/<calle>/<num>/<loc>/', agregar_envio),
]
