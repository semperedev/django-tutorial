from django.urls import path

from .views import VistaIndice, VistaLista, VistaDetalle

urlpatterns = [
    path('', VistaIndice.as_view(), name='indice'),
    path('entradas/', VistaLista.as_view(), name='lista'),
    path('entradas/<pk>/', VistaDetalle.as_view(), name='detalle'),
]
