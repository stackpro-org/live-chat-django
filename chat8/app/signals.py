
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
import random



@receiver(post_save, sender=User)
def create_profile(sender, instance, created,  **kwargs):

    if created:

        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
           

        )