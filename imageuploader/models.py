from django.db import models
from django.conf import settings
from uuid import uuid4
User = settings.AUTH_USER_MODEL

def upload_to(instance, filename):
    location = str(instance.user.username)
    return "%s/%s" %(location, filename)
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(upload_to="media/", null=True, blank=True)

    def __init__(self):
        return self.user.username