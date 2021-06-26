from django.urls import path

from ExamPrep.expenses.views import home_page, create_expense, edit_expense, delete_expense, profile, profile_edit, \
    profile_delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create_expense, name='create'),
    path('edit/<int:pk>', edit_expense, name='edit'),
    path('delete/<int:pk>', delete_expense, name='delete'),
    path('profile/', profile, name="profile"),
    path('profile/edit', profile_edit, name='profile_edit'),
    path('profile/delete', profile_delete, name='profile_delete')
]