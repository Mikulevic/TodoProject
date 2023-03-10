from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
