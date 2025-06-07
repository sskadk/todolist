from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .models import Type

def home(request):
    TodoList = Todo.objects.all()
    return render(request, 'index.html', context={'Tasks': TodoList})

def type(request):
    types = Type.objects.all()
    return render(request, 'type.html', context={'types': types})
