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
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_status = request.POST.get('task_status')

        Todo.objects.create(task_name=task_name, 
                            task_description=task_description, 
                            task_status=task_status)
        
    return render(request, 'create_todo.html')