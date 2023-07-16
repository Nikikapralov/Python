from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=15, validators=[MaxLengthValidator(15)])
    last_name = models.CharField(max_length=15, validators=[MaxLengthValidator(15)])
    budget = models.IntegerField()


class Expense(models.Model):
    title = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()