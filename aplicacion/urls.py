from aplicacion import views
from django.urls import path



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('cliente/', views.cliente, name='cliente'),
    path('producto/', views.producto, name='producto'),
    path('envio/', views.envio, name='envio'),
    path('clienteform/', views.clienteform, name='clienteform'),
    path('productoform/', views.productoform, name='productoform'),
    path('envioform/', views.envioform, name='envioform'),
    path('busquedanombre/', views.busquedanombre, name='busquedanombre'),
    path('buscar/', views.buscar),
  

]