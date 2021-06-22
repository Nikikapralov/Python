from django.shortcuts import render, redirect

# Create your views here.
from Todo.todoapp.models import Todo
from Todo.todoapp.forms import FormTodo


def success(request):
    return render(request, 'success.html')


def landing_page(request):
    everything = Todo.objects.all()
    data = {'todos': everything}
    return render(request, 'landing_page.html', context=data)


def index(request):
    everything = Todo.objects.all()
    data = {'todos': everything}
    return render(request, 'index.html', context=data)


def create_todo(request):
    if request.method == 'GET':
        form = FormTodo()
        context = {"todos": form}
        return render(request, 'create.html', context=context)
    form = FormTodo(request.POST)
    if form.is_valid():
        new_todo = Todo(**form.cleaned_data)
        print(form.cleaned_data["is_done"])
        new_todo.save()
        return redirect('/')

    context = {"todos": form}
    return render(request, "create.html", context=context)


def edit_todo(request, pk):
    if request.method == 'GET':
        form = FormTodo()
        context = {"todos": form}
        return render(request, 'create.html', context=context)
    form = FormTodo(request.POST)
    todo_to_edit = Todo.objects.get(pk=pk)

    if form.is_valid():
        todo_to_edit.delete()
        new_todo = Todo(**form.cleaned_data)
        new_todo.save()
        return redirect('landing_page')

    context = {"todos": form}
    return render(request, "create.html", context=context)


def delete_todo(request, pk):
    to_delete = Todo.objects.get(pk=pk)
    to_delete.delete()
    return redirect('success')