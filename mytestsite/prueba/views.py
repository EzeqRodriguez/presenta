# from django.shortcuts import render
# from django.shortcuts import render, HttpResponse

# Create your views here.

# from django.contrib import admin
# from django.urls import path


from django.shortcuts import render



def bienvenida(request):
    return render(request, 'prueba/index.html')

