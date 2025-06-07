from django.contrib import admin
from .models import Todo
from .models import Type

admin.site.register(Todo)
admin.site.register(Type)
