from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/', blank=True, null=True)
    baker = models.ForeignKey('Baker', on_delete=models.CASCADE, related_name='cakes')

    def __str__(self):
        return f'{self.name} {self.price} {self.description}'


class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
