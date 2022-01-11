from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def taskList(request):
    tasks_list = Task.objects.all().order_by('-created_at')

    paginator = Paginator(tasks_list, 5)

    page = request.GET.get('page')

    tasks = paginator.get_page(page)

    return render(request, 'paginas/list.html', {'tasks': tasks})
@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'paginas/task.html', {'task':task})
@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            messages.info(request, 'Atividade criada com sucesso.')
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'paginas/addtask.html', {'form': form})
@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)


    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        messages.info(request, 'Atividade editada com sucesso.')
        if(form.is_valid()):
            task.save()
            return redirect('/')
            
        else:
            return render(request, 'paginas/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'paginas/edittask.html', {'form': form, 'task': task})
@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Atividade deletada com sucesso.')

    return redirect('/')



class PaginaInicial(TemplateView):
    template_name = 'index.html'