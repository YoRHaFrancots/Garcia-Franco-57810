from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"entidades/index.html")
def clientes(request):
    contexto={"clientes":Cliente.objects.all()}
    return render(request,"entidades/clientes.html",contexto)
@login_required
def pedidos(request):
    contexto={"pedidos":Pedido.objects.all()}
    return render(request,"entidades/pedidos.html",contexto)
@login_required
def productos(request):
    contexto={"productos":Producto.objects.all()}
    return render(request,"entidades/productos.html",contexto)

#Producto
@login_required
def productoForm(request):
    if request.method == "POST":
        miForm=ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre=miForm.cleaned_data.get("nombre")
            producto_precio=miForm.cleaned_data.get("precio")
            producto_stock=miForm.cleaned_data.get("stock")
            producto= Producto(nombre=producto_nombre,precio=producto_precio,stock=producto_stock)
            producto.save()
            contexto={"productos":Producto.objects.all()}
            return render(request,"entidades/productos.html",contexto)
       
    else:
        miForm = ProductoForm()
    
    return render(request, "entidades/productoForm.html", {"form": miForm})
@login_required
def productoUpdate(request, id_producto):
    producto= Producto.objects.get(id=id_producto)
    if request.method== "POST":
          miForm=ProductoForm(request.POST)
          if miForm.is_valid():
            producto.nombre=miForm.cleaned_data.get("nombre")
            producto.precio=miForm.cleaned_data.get("precio")
            producto.stock=miForm.cleaned_data.get("stock")
            
            producto.save()
            contexto={"productos":Producto.objects.all()}
            return render(request,"entidades/productos.html",contexto)
    else:
        miForm=ProductoForm(initial={"nombre":producto.nombre,"precio":producto.precio,"stock":producto.stock})
        return render(request, "entidades/productoForm.html", {"form": miForm})
@login_required    
def productoDelete(request, id_producto):
    producto= Producto.objects.get(id=id_producto)
    producto.delete()
    contexto={"productos":Producto.objects.all()}
    return render(request,"entidades/productos.html",contexto)
#Cliente

def clienteForm(request):
    if request.method == "POST":
        miForm=ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre=miForm.cleaned_data.get("nombre")
            cliente_apellido=miForm.cleaned_data.get("apellido")
            cliente_email=miForm.cleaned_data.get("email")
            cliente= Cliente(nombre=cliente_nombre,apellido=cliente_apellido,email=cliente_email)
            cliente.save()
            contexto={"clientes":Cliente.objects.all()}
            return render(request,"entidades/clientes.html",contexto)
       
    else:
        miForm = ClienteForm()
    
    return render(request, "entidades/clienteForm.html", {"form": miForm})
@login_required
def clienteUpdate(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    if request.method== "POST":
          miForm=ClienteForm(request.POST)
          if miForm.is_valid():
            cliente.nombre=miForm.cleaned_data.get("nombre")
            cliente.apellido=miForm.cleaned_data.get("apellido")
            cliente.email=miForm.cleaned_data.get("email")
            
            cliente.save()
            contexto={"clientes":Cliente.objects.all()}
            return render(request,"entidades/clientes.html",contexto)
    else:
        miForm=ClienteForm(initial={"nombre":cliente.nombre,"apellido":cliente.apellido,"email":cliente.email})
        return render(request, "entidades/clienteForm.html", {"form": miForm})
@login_required    
def clienteDelete(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    cliente.delete()
    contexto={"clientes":Cliente.objects.all()}
    return render(request,"entidades/clientes.html",contexto)
#Pedido
@login_required
def pedidoForm(request):
    if request.method == "POST":
        miForm=PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_descripcion=miForm.cleaned_data.get("descripcion")
            pedido_direccion=miForm.cleaned_data.get("direccion")
            pedido_fechaEntrega=miForm.cleaned_data.get("fechaEntrega")
            pedido_entregado=miForm.cleaned_data.get("entregado")
            pedido= Pedido(descripcion=pedido_descripcion,direccion=pedido_direccion,fechaEntrega=pedido_fechaEntrega,entregado=pedido_entregado)
            pedido.save()
            contexto={"pedidos":Pedido.objects.all()}
            return render(request,"entidades/pedidos.html",contexto)
       
    else:
        miForm = PedidoForm()
    
    return render(request, "entidades/pedidoForm.html", {"form": miForm})
@login_required
def pedidoUpdate(request, id_pedido):
    pedido= Pedido.objects.get(id=id_pedido)
    if request.method== "POST":
          miForm=PedidoForm(request.POST)
          if miForm.is_valid():
            pedido.descripcion=miForm.cleaned_data.get("descripcion")
            pedido.direccion=miForm.cleaned_data.get("direccion")
            pedido.fechaEntrega=miForm.cleaned_data.get("fechaEntrega")
            pedido.entregado=miForm.cleaned_data.get("entregado")
            pedido.save()
            contexto={"pedidos":Pedido.objects.all()}
            return render(request,"entidades/pedidos.html",contexto)
    else:
        miForm=PedidoForm(initial={"descripcion":pedido.descripcion,"direccion":pedido.direccion,"fechaEntrega":pedido.fechaEntrega,"entregado":pedido.entregado})
        return render(request, "entidades/pedidoForm.html", {"form": miForm})
@login_required    
def pedidoDelete(request, id_pedido):
    pedido= Pedido.objects.get(id=id_pedido)    
    pedido.delete()
    contexto={"pedidos":Pedido.objects.all()}
    return render(request,"entidades/pedidos.html",contexto)
#Buscar producto
@login_required
def buscarProductos(request):
    return render(request,"entidades/buscar.html")
@login_required
def encontrarProductos(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        productos=Producto.objects.filter(nombre__icontains=patron)
        contexto={"productos":productos}
    else:
        contexto={"productos":Producto.objects.all()}
        
    return render(request,"entidades/productos.html",contexto)
    
  #Login - Logout - register

def loginRequest(request):
    if request.method== "POST":
        usuario= request.POST["username"]
        clave=request.POST["password"]
        user=authenticate(request,username=usuario,password=clave)
        if user is not None:
            login(request,user)
            #Recuperar avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request,"entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm=AuthenticationForm()
        return render(request,"entidades/login.html",{"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})
# Edit profile / Avatar

 

@login_required
def editProfile(request):

    usuario = request.user

    if request.method == "POST":

        miForm = UserEditForm(request.POST)

        if miForm.is_valid():

            user = User.objects.get(username=usuario)

            user.email = miForm.cleaned_data.get("email")

            user.first_name = miForm.cleaned_data.get("first_name")

            user.last_name = miForm.cleaned_data.get("last_name")

            user.save()

            return redirect(reverse_lazy("home"))

    else:

        miForm = UserEditForm(instance=usuario)

    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #Borrar Avatares
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #Enviar imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})
    