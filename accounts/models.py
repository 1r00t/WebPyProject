from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=255, blank=True, null=True)
    USER_ROLES = (
        ('A', 'Admin'),
        ('U', 'User'),
        ('Q', 'Questioneer'),
    )
    role = models.CharField(max_length=1, choices=USER_ROLES, default='U')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

Nostrud adipisicing cupidatat commodo cupidatat veniam ex enim ea mollit dolor reprehenderit mollit non.

Laboris quis id velit minim sit magna laboris ullamco. Ipsum id non nulla laboris enim proident voluptate in irure tempor officia commodo amet occaecat. Ipsum aliqua consectetur Lorem eiusmod cillum cillum ea ex duis.