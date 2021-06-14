from django.urls import path

from Todo.todoapp.views import landing_page

urlpatterns = [
    path('', landing_page)
]