from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required

def bienvenida(request):
    return render(request, 'prueba/index.html' )

