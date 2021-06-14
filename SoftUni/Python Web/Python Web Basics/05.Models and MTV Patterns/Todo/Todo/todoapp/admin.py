from django.contrib import admin

# Register your models here.
from Todo.todoapp.models import Todo

admin.site.register(Todo)