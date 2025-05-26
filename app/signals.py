import random

from django.dispatch import receiver
from django.db.models.signals import pre_delete

from app.models import Baker, Cake

@receiver(pre_delete, sender=Baker)
def delete_baker(sender, instance, **kwargs):
    cakes = Cake.objects.filter(baker = instance)
    bakers = Baker.objects.exclude(id = instance.id).all()

    for cake in cakes:
        new_baker = random.choice(bakers)
        cake.baker = new_baker
        cake.save()