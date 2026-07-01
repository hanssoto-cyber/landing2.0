from django.contrib import admin
from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'leido', 'creado')
    list_filter = ('leido',)
    search_fields = ('nombre', 'email', 'mensaje')