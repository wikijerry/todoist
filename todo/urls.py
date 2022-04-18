from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todoapp/',views.todoapp), 
    path('addTodoItems/',views.addTodoView),
    path('deleteTodoItems/<int:i>/', views.deleteTodoView),
     
]
