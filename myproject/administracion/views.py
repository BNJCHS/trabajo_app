# administracion/views.py

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola desde la app Administración")
