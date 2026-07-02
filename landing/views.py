from django.shortcuts import render, redirect
from django.contrib import messages
from itertools import groupby
from .models import Certificacion, Estadistica, Habilidad
from proyectos.models import Proyecto
from blog.models import Post
from contacto.forms import MensajeForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            send_mail(
                subject=f'Nuevo mensaje de {mensaje.nombre}',
                message=f'De: {mensaje.nombre} <{mensaje.email}>\n\n{mensaje.mensaje}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, '¡Mensaje enviado! Te responderé pronto.')
            return redirect('/#contacto')
    else:
        form = MensajeForm()

    habilidades = Habilidad.objects.all()
    skills_por_categoria = []
    for categoria, items in groupby(habilidades, key=lambda h: h.get_categoria_display()):
        skills_por_categoria.append((categoria, list(items)))

    context = {
        'certificaciones': Certificacion.objects.all(),
        'estadisticas': Estadistica.objects.all(),
        'skills_por_categoria': skills_por_categoria,
        'proyectos': Proyecto.objects.all(),
        'posts': Post.objects.filter(publicado=True)[:3],
        'form': form,
    }
    return render(request, 'landing/home.html', context)