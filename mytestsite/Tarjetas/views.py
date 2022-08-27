from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cliente
# Create your views here.
@login_required
def tarjetas(request):
    
    tarje=Cliente.objects.filter(customer_dni=(request.user))
    return render(request, 'Tarjetas/tarjetas.html', {"tarje":tarje},)