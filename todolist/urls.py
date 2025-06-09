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
]
