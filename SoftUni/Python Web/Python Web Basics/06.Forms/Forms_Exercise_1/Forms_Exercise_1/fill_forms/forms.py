from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, MinLengthValidator

from Forms_Exercise_1.fill_forms.validators import name_fst_letter_capital, password_only_letters_and_numbers


class FormUser(forms.Form):
    name = forms.CharField(max_length=30, validators=[MinLengthValidator(6), name_fst_letter_capital,])
    age = forms.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8),
                                                                       password_only_letters_and_numbers])
    email = forms.EmailField(widget=forms.EmailInput, validators=[EmailValidator],
                             error_messages={"invalid": 'Wrong maaul'})
    text = forms.CharField(max_length=200, widget=forms.Textarea)
    bot_field = forms.CharField(max_length=1000, widget=forms.HiddenInput, required=False)

    def clean_bot_field(self):
        data = self.cleaned_data['bot_field']
        if len(data) > 0:
            raise ValidationError('Bot')
        return data
