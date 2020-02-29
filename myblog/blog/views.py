from django.views.generic import DetailView, ListView, TemplateView

from .models import Entrada


class VistaIndice(TemplateView):
    template_name = 'index.html'


class VistaLista(ListView):
    model = Entrada


class VistaDetalle(DetailView):
    model = Entrada
