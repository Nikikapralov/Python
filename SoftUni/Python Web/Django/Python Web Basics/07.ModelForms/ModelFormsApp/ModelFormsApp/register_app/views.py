from django.shortcuts import render, redirect

# Create your views here.
from ModelFormsApp.register_app.forms import BookForm
from ModelFormsApp.register_app.models import BookModel


def index(request):
    books = BookModel.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            'form': BookForm()
        }
        return render(request, 'create.html', context)
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': BookForm()
    }
    return render(request, 'create.html', context)


def edit(request, pk):
    model_form_to_edit = BookModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=model_form_to_edit,
                        initial=model_form_to_edit.__dict__,
                        )
        for name, field in form.fields.items():
            if name == 'title':
                field.widget.attrs['readonly'] = True
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)
    form = BookForm(request.POST, instance=model_form_to_edit, initial=model_form_to_edit.__dict__)
    if form.is_valid():
        form.save()
        return redirect('index')
    form = BookForm(instance=model_form_to_edit, initial=model_form_to_edit.__dict__)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)

