from django.shortcuts import render

def vista_indice(request):
    return render(request, 'index.html')
