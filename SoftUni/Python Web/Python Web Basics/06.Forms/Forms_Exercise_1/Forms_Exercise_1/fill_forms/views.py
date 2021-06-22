from django.shortcuts import render, redirect
from Forms_Exercise_1.fill_forms.forms import FormUser
from Forms_Exercise_1.fill_forms.models import User
# Create your views here.


def success(request, pk):
    new_user = User.objects.get(pk=pk)
    context = {"user": new_user}
    return render(request, 'success.html', context)


def form_page(request):
    if request.method == 'GET':
        form = FormUser()
        context = {'form': form
        }
        return render(request, 'fill_data.html', context)

    form = FormUser(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        data = User(text=text, name=name, age=age, password=password, email=email)
        data.save()
        return redirect('success', pk=data.pk)
    context = {'form': form}
    return render(request, 'fill_data.html', context)