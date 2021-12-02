from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'index.html'

def taskList(request):
    return render(request, 'paginas/list.html')

def yourName(request, name):
    return render(request, 'paginas/yourname.html', {'name': name})