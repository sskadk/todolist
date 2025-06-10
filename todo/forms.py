from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            "task_name" : forms.Textarea(attrs={"class":"form-control"}),
            "task_description" : forms.Textarea(attrs={"class":"form-control"}),
            "task_status" : forms.Select(attrs={'class': 'form-select'},choices = (('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Pending', 'Pending'))),
        }