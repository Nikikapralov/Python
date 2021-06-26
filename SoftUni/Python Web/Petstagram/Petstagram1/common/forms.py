from django import forms

from Petstagram1.common.models import CommentModel


class CommentForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control rounded-2'}))
    pet_pk = forms.IntegerField(widget=forms.HiddenInput())
