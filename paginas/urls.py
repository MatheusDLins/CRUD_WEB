from django.urls import path
from .views import PaginaInicial
from . import views

urlpatterns = [
    #path('endereço/', minhaview.as_view(), name='nome-da-url'),
    path('home', PaginaInicial.as_view(), name='index'),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name')
]