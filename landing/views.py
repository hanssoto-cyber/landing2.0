from django.shortcuts import render
from .models import Certificacion, Estadistica


def home(request):
    context = {
        'certificaciones': Certificacion.objects.all(),
        'estadisticas': Estadistica.objects.all(),
    }
    return render(request, 'landing/home.html', context)