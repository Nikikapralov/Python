from django.urls import path
from DjangoProject.main_app.views import index

urlpatterns = [
    path('', index)
]