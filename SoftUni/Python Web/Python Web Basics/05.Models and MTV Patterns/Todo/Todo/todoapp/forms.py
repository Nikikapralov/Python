from django import forms
from django.core.validators import MaxLengthValidator


class FormTodo(forms.Form):
    title = forms.CharField(max_length=30, validators=[MaxLengthValidator(30)], label='Title')
    description = forms.CharField(max_length=200, widget=forms.Textarea(), required=False)
    is_done = forms.BooleanField(widget=forms.RadioSelect(choices=(("True", "True"), ("False", "False"))), required=False)