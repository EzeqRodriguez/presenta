from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def prestamos(request):
    return render(request, 'Prestamos/prestamos.html')