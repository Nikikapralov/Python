from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(130), MinValueValidator(18)])
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    text = models.TextField(max_length=200, null=True, blank=True)