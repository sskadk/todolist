from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .models import Type

def home(request):
    return render(request, 'index.html')

def todo_view(request):
    TodoList = Todo.objects.all()
    return render(request, 'todo_page.html', context={'Tasks': TodoList})

def type_view(request):
    types = Type.objects.all()
    return render(request, 'type_page.html', context={'types': types})

def create_todo_view(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_status = request.POST.get('task_status')

        Todo.objects.create(task_name=task_name, 
                            task_description=task_description, 
                            task_status=task_status)
        
    return render(request, 'create_todo.html')


def create_type_view(request):
    if request.method == 'POST':
        type_name = request.POST.get('type_name')
        type_description = request.POST.get('type_description')

        Type.objects.create(type_name=type_name,
                            type_description=type_description,)
                                
    return render(request, 'create_type.html')