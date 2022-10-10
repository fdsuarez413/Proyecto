from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from modulos.models import Tipopqrs

from users.models import User

class PQRSForm(forms.Form):
    Nombre = forms.CharField(max_length=150, required=True)
    Apellido = forms.CharField(max_length=150, required=True)
    tel = forms.IntegerField(required=True)
    Descripcion = forms.CharField(required=True, widget=forms.Textarea(attrs={"row:5 'cols":20}))
    email = forms.EmailField(max_length=150, required=True)
    Tipopqrs = forms.ModelChoiceField(label="Tipo", queryset=Tipopqrs.objects.all())

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario')
    name = forms.CharField(label='Nombre')
    surname = forms.CharField(label='Apellido')
    document = forms.IntegerField(label='Numero de documento')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'document', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}