from django.contrib import admin

from .models import Entrada


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto')
