from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', home,name="home"),
  path('about/',about,name="about"),
  path('clientes/', clientes,name="clientes"),
  path('productos/', productos,name="productos"),
  path('pedidos/', pedidos,name="pedidos"),
  #Producto
  path('productoForm/', productoForm,name="productoForm"),
  path('productoUpdate/<id_producto>/', productoUpdate,name="productoUpdate"),
  path('productoDelete/<id_producto>/', productoDelete,name="productoDelete"),
  #Cliente
  path('clienteForm/', clienteForm,name="clienteForm"),
  path('clienteUpdate/<id_cliente>/', clienteUpdate,name="clienteUpdate"),
  path('clienteDelete/<id_cliente>/', clienteDelete,name="clienteDelete"),
  #Pedido
  path('pedidoForm/', pedidoForm,name="pedidoForm"),
  path('pedidoUpdate/<id_pedido>/', pedidoUpdate,name="pedidoUpdate"),
  path('pedidoDelete/<id_pedido>/', pedidoDelete,name="pedidoDelete"),
  #Search
  path('buscarProductos/', buscarProductos,name="buscarProductos"),
  path('encontrarProductos/', encontrarProductos,name="encontrarProductos"),
  #Login - Logout - Register
  path('login/', loginRequest,name="login"),
  path('logout/',LogoutView.as_view(template_name="entidades/logout.html"),name="logout"),
  path('register/', register,name="register"),
  #Edit profile / Avatar

  path('perfil/', editProfile, name="perfil"),
  path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
  path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]