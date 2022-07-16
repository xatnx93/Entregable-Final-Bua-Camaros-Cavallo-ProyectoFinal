from django.shortcuts import redirect, render
from ProyectoFinalApp.models import *
from ProyectoFinalApp.forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import (
    login,
    logout as django_logout,
    authenticate,
    update_session_auth_hash,
)
from django.contrib import messages


def inicio(request):
    return render(
        request,
        "index.html",
    )


def inscripcion(request):

    return render(request, "inscripcion.html", {})


def inicial_descripcion(request):

    return render(request, "curso_inicial.html", {})


def intermedio_descripcion(request):

    return render(request, "curso_intermedio.html", {})


def avanzado_descripcion(request):

    return render(request, "curso_avanzado.html", {})


def sobre_nosotros(request):

    return render(request, "about_us.html", {})


def agregar_inicial(request):

    if request.method == "POST":

        curso1 = FormularioInicial(request.POST)

        if curso1.is_valid():

            informacion = curso1.cleaned_data

            curso1 = ClaseInicial(
                nombre1_clase=informacion["nombre1_form"],
                apellido1_clase=informacion["apellido1_form"],
                email1_clase=informacion["email1_form"],
                celular1_clase=informacion["celular1_form"],
            )

            curso1.save()

            return render(request, "index.html")

    else:
        curso1 = FormularioInicial()

    return render(request, "formulario_inicial.html", {"form": curso1})


def agregar_intermedio(request):

    if request.method == "POST":

        curso2 = FormularioIntermedio(request.POST)

        if curso2.is_valid():

            informacion = curso2.cleaned_data

            curso2 = ClaseIntermedia(
                nombre2_clase=informacion["nombre2_form"],
                apellido2_clase=informacion["apellido2_form"],
                email2_clase=informacion["email2_form"],
                celular2_clase=informacion["celular2_form"],
            )

            curso2.save()

            return render(request, "index.html")

    else:
        curso2 = FormularioIntermedio()

    return render(request, "formulario_intermedio.html", {"form": curso2})


def agregar_avanzado(request):

    if request.method == "POST":

        curso3 = FormularioAvanzado(request.POST)

        if curso3.is_valid():

            informacion = curso3.cleaned_data

            curso3 = ClaseAvanzada(
                nombre3_clase=informacion["nombre3_form"],
                apellido3_clase=informacion["apellido3_form"],
                email3_clase=informacion["email3_form"],
                celular3_clase=informacion["celular3_form"],
            )

            curso3.save()

            return render(request, "index.html")

    else:
        curso3 = FormularioAvanzado()

    return render(request, "formulario_avanzado.html", {"form": curso3})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("get_login")
        else:
            return redirect("get_login")

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def register_request(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("get_login")

        return render(request, "register.html", {"form": form})

    form = UserRegisterForm()

    return render(request, "register.html", {"form": form})


def logout(request):

    django_logout(request)

    return redirect("inicio")


def user_info(request):

    return render(request, "user.html", {})


def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)
            messages.success(request, "Cambiaste tu password!")

            return redirect("inicio")

        else:

            messages.error(request, "Por favor, corregi el error.")

    else:

        form = PasswordChangeForm(request.user)

    return render(request, "change_password.html", {"form": form})


def store(request):

    itemsitos = Items.objects.all()

    return render(request, "tienda.html", {"itemsitos": itemsitos})


# def store(request):

#     if request.method == "GET":

#         itemsitos = ItemForm(request.GET)

#         if itemsitos.is_valid():

#             informacion = itemsitos.cleaned_data

#             itemsitos = Items(
#                 titulo=informacion["titulo_form"],
#                 marca=informacion["marca_form"],
#                 imagen=informacion["imagen_form"],
#                 precio=informacion["precio_form"],
#             )

#             itemsitos.save()

#             return render(request, "index.html")

#     else:
#         itemsitos = FormularioIntermedio()

#     return render(request, "tienda.html", {"form": itemsitos})
