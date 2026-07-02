from django.contrib import admin
from .models import Certificacion, Estadistica, Habilidad


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'fecha')
    ordering = ('-fecha',)


@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ('etiqueta', 'valor', 'orden')
    ordering = ('orden',)


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'orden')
    list_filter = ('categoria',)
    ordering = ('categoria', 'orden')