from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.


def pages_positive_not_zero_validator(pages):
    if pages <= 0:
        raise ValidationError('Pages cannot be 0 or less.')


class BookModel(models.Model):
    title = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    pages = models.IntegerField(default=0, validators=[pages_positive_not_zero_validator])
    description = models.CharField(max_length=100, validators=[MaxLengthValidator(100)], default='')
    author = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])