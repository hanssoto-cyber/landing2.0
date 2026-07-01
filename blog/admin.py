from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'publicado', 'creado')
    list_filter = ('categoria', 'publicado')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}