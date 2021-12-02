from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'paginas/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'paginas/task.html', {'task':task})


class PaginaInicial(TemplateView):
    template_name = 'index.html'


def yourName(request, name):
    return render(request, 'paginas/yourname.html', {'name': name})