from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioInicial(forms.Form):
    nombre1_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido1_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email1_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular1_form = forms.IntegerField(
        label="Tu Celular: ",
    )


class FormularioIntermedio(forms.Form):
    nombre2_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido2_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email2_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular2_form = forms.IntegerField(
        label="Tu Celular: ",
    )


class FormularioAvanzado(forms.Form):
    nombre3_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido3_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email3_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular3_form = forms.IntegerField(
        label="Tu Celular: ",
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_texts = {k: "" for k in fields}


class ItemForm(forms.Form):
    titulo_form = forms.CharField(max_length=50)
    marca_form = forms.CharField(max_length=20)
    imagen_form = forms.ImageField()
    precio_form = forms.DecimalField(max_digits=9, decimal_places=0)
    url_form = models.URLField(max_length=250)
