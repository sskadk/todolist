from django.contrib import admin
from django.urls import path
from todo.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('todo/', todo_view),
    path('type/', type_view),
    path('create_todo/', create_todo_view),
    path('create_type/', create_type_view),
    path('update_todo/<int:pk>/', update_todo_view, name="update-todo"),
    path('delete_todo/<int:pk>/', delete_todo_view, name="delete-todo"),
    path('update_type/<int:pk>/', update_type_view, name="update-type"),
    path('delete_type/<int:pk>/', delete_type_view, name="delete-type"),
]
