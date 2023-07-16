from django.shortcuts import render, redirect

# Create your views here.
from Petstagram1.common.forms import CommentForm
from Petstagram1.pets.forms import CreatePetForm
from Petstagram1.pets.models import Pet, Like


def apply_bootstrap_class(bs_class, form_class, instance=None, initial=None):
    form = form_class(instance=instance, initial=initial)
    for name, field in form.fields.items():
        field.widget.attrs['class'] = bs_class
    return form


def pet_all(request):
    all_pets = Pet.objects.all()
    context = {
        'all_pets': all_pets
    }
    return render(request, 'pet_list.html', context=context)


def pet_detail(request, pet_id):
    if request.method == 'POST':

        form_com = CommentForm(request.POST)
        if form_com.is_valid():
            pet = Pet.objects.get(pk=pet_id)
            form = CommentForm(form_com.cleaned_data['comment'])
            form.pet = pet
            form.save()
            return redirect('details')
        pet = Pet.objects.get(pk=pet_id)
        comments = pet.commentmodel_set.all()
        context = {
            'pet': pet,
            'all_likes': pet.like_set.count(),
            'comments': comments,
            'form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)
    pet = Pet.objects.get(pk=pet_id)
    comments = pet.commentmodel_set.all()
    context = {
        'pet': pet,
        'all_likes': pet.like_set.count(),
        'comments': comments,
        'form': CommentForm(),
    }
    return render(request, 'pet_detail.html', context)


def like_pet(request, pet_id):
    pet_to_like = Pet.objects.get(pk=pet_id)
    like = Like(pet_id=pet_to_like)
    like.save()
    return redirect('details', pet_id)


def create_pet(request):
    form = apply_bootstrap_class('form-control', CreatePetForm)
    context = {'form': form}
    if request.method == 'POST':
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pets')
        return render(request, 'pet_create.html', context)

    return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet_data = Pet.objects.get(pk=pk)
    form = apply_bootstrap_class('form-control', CreatePetForm, instance=pet_data, initial=pet_data.__dict__)
    context = {"form": form}
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=pet_data)
        if form.is_valid():
            form.save()
            return redirect('details')
        return render(request, 'pet_edit.html', context)
    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet_to_delete = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet_to_delete.delete()
        return redirect('list_pets')
    return render(request, 'pet_delete.html')
