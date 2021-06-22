from django.urls import path
from Petstagram1.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page')
]