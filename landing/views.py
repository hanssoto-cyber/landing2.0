from django.shortcuts import render
from itertools import groupby
from .models import Certificacion, Estadistica, Habilidad


def home(request):
    habilidades = Habilidad.objects.all()
    # Agrupar por categoría (ya vienen ordenadas por categoria+orden desde el modelo)
    skills_por_categoria = []
    for categoria, items in groupby(habilidades, key=lambda h: h.get_categoria_display()):
        skills_por_categoria.append((categoria, list(items)))

    context = {
        'certificaciones': Certificacion.objects.all(),
        'estadisticas': Estadistica.objects.all(),
        'skills_por_categoria': skills_por_categoria,
    }
    return render(request, 'landing/home.html', context)