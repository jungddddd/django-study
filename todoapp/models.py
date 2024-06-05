from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length = 500)
    priority = models.IntegerField(default=1)
    image = models.ImageField(upload_to='todo/', null=False)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='todo/', null=False)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


