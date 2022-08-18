from django.shortcuts import render

# Create your views here.

def clientes(request):
    return render(request, 'Clientes/clientes.html')