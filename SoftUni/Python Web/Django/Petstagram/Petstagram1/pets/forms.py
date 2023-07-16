from django import forms

from Petstagram1.pets.models import Pet


class CreatePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

