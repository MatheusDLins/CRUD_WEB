from django.urls import path
from .views import PaginaInicial
from . import views

urlpatterns = [
    #path('endereço/', minhaview.as_view(), name='nome-da-url'),
    path('home', PaginaInicial.as_view(), name='index'),
    path('', views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]