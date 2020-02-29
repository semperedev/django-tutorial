from django.urls import path

from .views import VistaIndice, VistaLista, VistaDetalle

urlpatterns = [
    path('', VistaIndice.as_view()),
    path('entradas/', VistaLista.as_view()),
    path('entrada/<pk>/', VistaDetalle.as_view()),
]
