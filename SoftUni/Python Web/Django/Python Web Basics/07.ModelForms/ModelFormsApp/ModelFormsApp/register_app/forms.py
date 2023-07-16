from django import forms

from ModelFormsApp.register_app.models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'pages': forms.NumberInput(attrs={'class': 'form-control'}),
                   'author': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}), }

