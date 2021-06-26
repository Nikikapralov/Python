from django import forms

from ExamPrep.expenses.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 10, 'cols': 40})}
