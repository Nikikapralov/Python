from django.shortcuts import render

# Create your views here.
from Todo.todoapp.models import Todo


def landing_page(request):
    everything = Todo.objects.all()
    data = {'todos': everything }
    return render(request, 'landing_page.html', context=data)