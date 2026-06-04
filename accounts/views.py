from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def products(request):
    productos_demo = [
        {"nombre": "Notebook Lenovo", "precio": "$650.000"},
        {"nombre": "Mouse inalámbrico", "precio": "$12.000"},
        {"nombre": "Teclado mecánico", "precio": "$45.000"},
        {"nombre": "Monitor 24 pulgadas", "precio": "$120.000"},
        {"nombre": "Audífonos Gamer", "precio": "$35.000"},
        {"nombre": "Webcam Full HD", "precio": "$28.000"},
        {"nombre": "Disco SSD 1TB", "precio": "$85.000"},
        {"nombre": "Tablet Samsung", "precio": "$220.000"},
        {"nombre": "Impresora Multifuncional", "precio": "$95.000"},
        {"nombre": "Silla Gamer", "precio": "$180.000"},
        {"nombre": "Smartwatch", "precio": "$75.000"},
        {"nombre": "Parlante Bluetooth", "precio": "$42.000"},
    ]
    return render(request, 'accounts/products.html', {"products" : productos_demo})