from django.urls import path

from .views import vista_indice

urlpatterns = [
    path('', vista_indice),
]
