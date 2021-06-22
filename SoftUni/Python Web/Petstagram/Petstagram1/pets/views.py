from django.shortcuts import render, redirect

# Create your views here.
from Petstagram1.pets.models import Pet, Like


def pet_all(request):
    all_pets = Pet.objects.all()
    context = {
        'all_pets': all_pets
    }
    return render(request, 'pet_list.html', context=context)


def pet_detail(request, pet_id):

    pet = Pet.objects.get(pk=pet_id)
    context = {
        'pet': pet,
        'all_likes': pet.like_set.count()
    }
    return render(request, 'pet_detail.html', context)


def like_pet(request, pet_id):
    pet_to_like = Pet.objects.get(pk=pet_id)
    like = Like(pet_id=pet_to_like)
    like.save()
    return redirect('details', pet_id)
