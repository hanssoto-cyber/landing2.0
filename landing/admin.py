from django.contrib import admin
from .models import Certificacion, Estadistica


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'fecha')
    ordering = ('-fecha',)


@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ('etiqueta', 'valor', 'orden')
    ordering = ('orden',)