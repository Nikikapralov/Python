from django.urls import path
from DjangoProject.secondary_app.views import index_2

urlpatterns = [
    path('', index_2)
]