from django.contrib import admin
from django.urls import path
from todo.views import home
from todo.views import type

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('type/', type),
]
