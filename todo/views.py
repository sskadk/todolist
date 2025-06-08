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

def create_todo_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name, description=description, status=status)
        
    return render(request, 'create_todo.html')