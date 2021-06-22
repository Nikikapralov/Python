from django.db import models

# Create your models here.


class Pet(models.Model):
    TYPE_CAT = 'Cat'
    TYPE_DOG = 'Dog'
    TYPE_PARROT = 'Parrot'
    CHOICES = (
        (TYPE_CAT, 'Cat'),
        (TYPE_DOG, 'Dog'),
        (TYPE_PARROT, 'Parrot')
    )

    type = models.CharField(max_length=6, choices=CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    image_url = models.URLField()


class Like(models.Model):
    pet_id = models.ForeignKey(to=Pet, on_delete=models.CASCADE)