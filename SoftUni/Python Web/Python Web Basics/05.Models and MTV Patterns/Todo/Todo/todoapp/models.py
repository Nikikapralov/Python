from django.db import models
import sys

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=sys.maxsize)
    is_done = models.BooleanField()
