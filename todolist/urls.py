from django.contrib import admin
from django.urls import path
from todo.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('todo/', todo_view, name="todo_list"),
    path('type/', type_view, name="type_list"),
    path('create_todo/', create_todo_view, name="create-todo"),
    path('create_type/', create_type_view, name="create-type"),
    path('update_todo/<int:pk>/', update_todo_view, name="update-todo"),
    path('todo/search/', search_todo_view, name='todo_search'),
    path('delete_todo/<int:pk>/', delete_todo_view, name="delete-todo"),
    path('update_type/<int:pk>/', update_type_view, name="update-type"),
    path('delete_type/<int:pk>/', delete_type_view, name="delete-type"),
]

