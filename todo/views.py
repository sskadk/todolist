from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .models import Type
from .forms import TodoForm
from .forms import TypeForm

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

def update_todo_view(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_form = TodoForm(instance=todo_obj)
    if request.method == "POST":
        todo_form = TodoForm(instance=todo_obj, data=request.POST)
        if todo_form.is_valid():
            todo_form.save()
    return render(request, 'update_todo.html', context={'form':todo_form})

def delete_todo_view(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('/todo')

def update_type_view(request, pk):
    type_obj = Type.objects.get(id=pk)
    type_form = TypeForm(instance=type_obj)
    if request.method == "POST":
        type_form = TypeForm(instance=type_obj, data=request.POST)
        if type_form.is_valid():
            type_form.save()
    return render(request, 'update_type.html', context={'form':type_form})

def delete_type_view(request, pk):
    type_obj = Type.objects.get(id=pk)
    type_obj.delete()
    return redirect('/type')