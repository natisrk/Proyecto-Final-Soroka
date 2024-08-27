from aplicacion import views
from django.urls import path



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cliente/', views.cliente, name='cliente'),
    path('producto/', views.producto, name='producto'),
    path('envio/', views.envio, name='envio'),
    path('busquedanombre/', views.busquedanombre, name='busquedanombre'),
    path('buscar/', views.buscar),
  

]