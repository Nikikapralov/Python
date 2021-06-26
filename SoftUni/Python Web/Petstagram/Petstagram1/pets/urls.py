from django.urls import path

from Petstagram1.pets.views import pet_all, pet_detail, like_pet, create_pet, edit_pet, delete_pet

urlpatterns = [
    path('list_pets/', pet_all, name='list_pets'),
    path('pet_details/<int:pet_id>', pet_detail, name='details'),
    path('like/<int:pet_id>', like_pet, name='like'),
    path('create_pet/', create_pet, name='create'),
    path('edit_pet/<int:pk>', edit_pet, name='edit'),
    path('delete_pet/<int:pk>', delete_pet, name='delete')
]