from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from uuid import uuid4
from django.dispatch import receiver
User = settings.AUTH_USER_MODEL

def upload_to(instance, filename):
    location = str(instance.user.username)
    return "%s/%s" %(location, filename)
class Profile(models.Model):
    EXPERIENCE_CHOICES = (
        ('Less than 1 yr', 'Less than 1 yr'),
        ('Less than 3 yr', 'Less than 3 yr'),
        ('More than 3 yr', 'More than 3 yr'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    birth_date=models.DateField(null=True, blank=True)
    career=models.CharField(max_length=250, blank=True)
    picture = models.ImageField(upload_to="media/", null=True, blank=True)
    is_a_programmer = models.BooleanField(default=True)
    went_to_what_school = models.CharField(max_length=50, blank=True)

User = property(lambda u: Profile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __init__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_or_update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #         instance.profile.save()   