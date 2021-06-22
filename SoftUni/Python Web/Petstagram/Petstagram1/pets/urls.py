from django.urls import path

from Petstagram1.pets.views import pet_all, pet_detail, like_pet

urlpatterns = [
    path('list_pets/', pet_all, name='list_pets'),
    path('pet_details/<int:pet_id>', pet_detail, name='details'),
    path('like/<int:pet_id>', like_pet, name='like')
]