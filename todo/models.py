from django.db import models


class Todo(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    task_status = models.CharField(max_length=50)

class Type(models.Model):
    type_name = models.CharField(max_length=300)
    type_description = type_description = models.TextField()
