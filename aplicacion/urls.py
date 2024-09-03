from aplicacion import views
from django.urls import path
from aplicacion import views_clases



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cliente/', views.cliente, name='cliente'),
    path('producto/', views.producto, name='producto'),
    path('envio/', views.envio, name='envio'),
    path('busquedanombre/', views.busquedanombre, name='busquedanombre'),
    path('buscar/', views.buscar),
    path('leerclientes/', views.leerclientes, name= 'leerclientes'), 
    path('eliminarcliente/<cliente_nombre>/', views.eliminarcliente, name= 'eliminarcliente'),
    path('about/', views.about, name='about'),
   
   
  
]

urls_vistas_clases = [
    path('clases/list/', views_clases.ProductoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.ProductoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete')
]

urlpatterns += urls_vistas_clases