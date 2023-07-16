from django.urls import path

from Todo.todoapp.views import landing_page, index, create_todo, edit_todo, delete_todo, success

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('index/', index, name='index'),
    path('create/', create_todo, name="create_todo"),
    path('edit/<int:pk>', edit_todo, name='update'),
    path('delete/<int:pk>', delete_todo, name='delete'),
    path('success/', success, name="success")
]