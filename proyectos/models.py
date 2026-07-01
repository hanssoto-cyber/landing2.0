from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(
        max_length=200,
        help_text="Separadas por coma, ej: Django, Docker, Bootstrap"
    )
    repo_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-destacado', '-creado']

    def __str__(self):
        return self.titulo

    def lista_tecnologias(self):
        return [t.strip() for t in self.tecnologias.split(',')]