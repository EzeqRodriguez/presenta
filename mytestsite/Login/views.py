from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


class registro(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "Login/crearUsuario.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():

            usuario=form.save()
        
            login(request, usuario)
    
            return redirect('principal')

        else:
            for errores in form.error_messages:
                messages.error(request, form.error_messages[errores])
            return render(request, "Login/crearUsuario.html",{"form":form})
    

def login1(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario and contra is not None:
                login(request, usuario)
                return redirect('principal')
            else:
                messages.error(request, "Datos incorrectos, Intente nuevamente")
        else:
            messages.error(request, "Datos incorrectos, Intente nuevamente")
    
    
    form = AuthenticationForm
    return render(request, "Login/login.html",{"form":form})



def cerrar(request):
    logout(request)
    return redirect('iniciar')



