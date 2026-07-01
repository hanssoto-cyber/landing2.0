from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@email.com'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje', 'rows': 5}),
        }