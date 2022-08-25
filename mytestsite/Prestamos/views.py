from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cliente, Tarjeta
# Create your views here.
from .forms import ContactForm

@login_required
def prestamos(request):
    
    
    presta=Cliente.objects.filter(customer_dni=(request.user))
    contact_form = ContactForm
    
    if request.method == 'POST':
        formulario = contact_form(request.POST)
        if formulario.is_valid():
            monto = formulario.cleaned_data['monto']
            if int(monto) >= 100000:
                return render(request, 'prestamos/prestamoR.html')
            else:
                # balance= Cliente.objects.all().values('balance')
                # nuevo_balance = balance + monto
                # # Cliente.save(nuevo_balance)
                # Cliente.save(nuevo_balance)
            


                return render(request, 'prestamos/prestamoA.html')
    
    return render(request, 'Prestamos/prestamos.html', {"prestamos":presta, 'form':contact_form})


@login_required
def prestamoA(request):
    return render(request, 'Prestamos/prestamoA.html')


@login_required
def prestamoR(request):
    return render(request, 'Prestamos/prestamoR.html')

