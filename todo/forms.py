from django.forms import ModelForm
from .models import Todo
from .models import Type
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
class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'
        widgets = {
            "type_name" : forms.Textarea(attrs={"class":"form-control"}),
            "type_description" : forms.Select(attrs={'class': 'form-select'},choices = (('Boolean', 'Boolean'), ('Integer', 'Integer'), ('Floating Point', 'Floating Point'), ('String', 'String'))),
        }

        