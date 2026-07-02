from django.db import models


class Certificacion(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField()
    credencial_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='certificaciones/', blank=True, null=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} - {self.institucion}"


class Estadistica(models.Model):
    etiqueta = models.CharField(max_length=50, help_text="Ej: Labs completados")
    valor = models.PositiveIntegerField(help_text="Ej: 15")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.valor} {self.etiqueta}"

class Habilidad(models.Model):
    CATEGORIAS = [
        ('seguridad', 'Herramientas de Seguridad'),
        ('lenguajes', 'Lenguajes de Programación'),
        ('redes', 'Redes'),
        ('web', 'Tecnologías Web'),
    ]

    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    icono = models.ImageField(upload_to='habilidades/')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['categoria', 'orden']
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"