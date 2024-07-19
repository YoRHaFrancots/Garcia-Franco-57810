from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True )
    email= forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   

class PedidoForm(forms.Form):
    descripcion=forms.CharField(max_length=500, required=True)
    direccion=forms.CharField(max_length=100, required=True)
    fechaEntrega=forms.DateField(required=True)
    entregado=forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
   
class RegistroForm(UserCreationForm):

    email = forms.EmailField(required=True)

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
  

 

    class Meta:

        model = User

        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):

    email = forms.EmailField(required=True)

    first_name = forms.CharField(label="Nombre", max_length=50, required=True)

    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

 

    class Meta:

        model = User

        fields = ["email", "first_name", "last_name"] 
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)