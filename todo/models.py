from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=300)

class Type(models.Model):
    name = models.CharField(max_length=300)