from django.contrib import admin
from django.urls import path, include
from .views import PaginaInicial, vendas
from . import views

from rest_framework import routers
from paginas.api import viewsets




route = routers.DefaultRouter()

route.register(r'task',viewsets.TaskWiewSet, basename="Task")


urlpatterns = [
    #path('endereço/', minhaview.as_view(), name='nome-da-url'),


    path('home', PaginaInicial.as_view(), name='index'),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('', include(route.urls)),
    path('vendas',views.vendas)
]