from django.db import models

# Create your models here.
from Petstagram1.pets.models import Pet


class CommentModel(models.Model):
    text = models.TextField(max_length=200)
    pet = models.ForeignKey(to=Pet, on_delete=models.CASCADE)
