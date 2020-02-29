from django.urls import path

from .views import VistaIndice, VistaLista

urlpatterns = [
    path('', VistaIndice.as_view()),
    path('entradas/', VistaLista.as_view()),
]
