from django.contrib import admin
from django.urls import path
from ProyectoFinalApp import views
from ProyectoFinalApp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("agregarinicial/", views.agregar_inicial, name="inicial"),
    path("agregarintermedio/", views.agregar_intermedio, name="intermedio"),
    path("agregaravanzado/", views.agregar_avanzado, name="avanzado"),
    path("inscribite/", views.inscripcion, name="inscripcion"),
    path("cursoinicial/", views.inicial_descripcion, name="inicial_des"),
    path("cursointermedio/", views.intermedio_descripcion, name="intermedio_des"),
    path("cursoavanzado/", views.avanzado_descripcion, name="avanzado_des"),
    path("sobrenosotros/", views.sobre_nosotros, name="sobre_nos"),
    path("login/", views.login_request, name="get_login"),
    path("registrate/", views.register_request, name="get_register"),
    path("logout/", views.logout, name="get_logout"),
    path("user/", views.user_info, name="my_info"),
    path("password/", views.change_password, name="cambio_password"),
    path("tienda/", views.store, name="tienda_online"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
