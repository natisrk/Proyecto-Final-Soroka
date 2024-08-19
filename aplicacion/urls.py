from aplicacion import views
from django.urls import path



urlpatterns = [
    path('inicio/', views.inicio),
    path('cliente/', views.cliente),
    path('producto/', views.producto),
    path('envio/', views.envio),
    
]