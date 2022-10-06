from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(self, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=User)
