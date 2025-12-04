from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from . import models

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance
    
    if created:
        models.Profile.objects.create(user = user,)