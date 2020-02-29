from django.views.generic import ListView, TemplateView

from .models import Entrada


class VistaIndice(TemplateView):
    template_name = 'index.html'


class VistaLista(ListView):
    model = Entrada
    template_name = 'entradas.html'
