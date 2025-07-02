from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')  # más adelante le pasamos productos
