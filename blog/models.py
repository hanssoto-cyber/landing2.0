from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    resumen = models.CharField(max_length=250, help_text="Aparece en el listado")
    contenido = models.TextField()
    categoria = models.CharField(
        max_length=50,
        help_text="Ej: SOC, Pentesting, Redes, CTF"
    )
    imagen = models.ImageField(upload_to='blog/', blank=True, null=True)
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detalle_post', kwargs={'slug': self.slug})