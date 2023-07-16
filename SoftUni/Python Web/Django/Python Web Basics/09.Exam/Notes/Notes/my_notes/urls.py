from django.urls import path

from Notes.my_notes.views import home_page, profile_page, profile_delete, add_note, edit_note, \
    delete_note, note_details

urlpatterns = [
    path('', home_page, name='home_page'),
    path('profile/', profile_page, name='profile'),
    path('profile/delete/', profile_delete, name='profile_delete'),
    path('add/', add_note, name='add_note'),
    path('edit<int:pk>/', edit_note, name='edit_note'),
    path('delete<int:pk>/', delete_note, name='delete_note'),
    path('details<int:pk>/', note_details, name='details')

]