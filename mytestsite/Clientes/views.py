from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cliente, Cuenta
# Create your views here.


@login_required
def clientes(request):
    
    clientesListados=Cliente.objects.filter(customer_dni=(request.user))
    
    return render(request, 'Clientes/clientes.html', {"clientes":clientesListados},)

