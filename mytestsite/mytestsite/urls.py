"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.contrib import admin
# from django.urls import path

from prueba.views import bienvenida

from Clientes.views import clientes

from Login.views import login1, registro, cerrar
from Prestamos.views import prestamos
from Tarjetas.views import tarjetas


urlpatterns = [
#  path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('principal', bienvenida, name='principal'),
    path('clientes',  clientes),
    path('iniciar',  login1, name='iniciar' ),
    path('prestamos', prestamos,  name='prestamos'),
    path('cerrar', cerrar,  name='cerrar'),
    path('tarjetas',  tarjetas),
    path('registro',  registro.as_view(), name="registrarse"),

]

