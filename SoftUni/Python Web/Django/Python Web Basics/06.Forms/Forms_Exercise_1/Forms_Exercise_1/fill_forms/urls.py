from django.urls import path

from Forms_Exercise_1.fill_forms.views import form_page, success

urlpatterns = [
    path('', form_page, name='form_page'),
    path('success/<int:pk>', success, name='success')

]