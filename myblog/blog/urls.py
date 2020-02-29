from django.urls import path

from .views import VistaIndice

urlpatterns = [
    path('', VistaIndice.as_view()),
]
