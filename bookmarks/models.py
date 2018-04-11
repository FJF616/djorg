from django.db import models
from uuid import uuid4

# Create your models here.
class Bookmark(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    notes = models.TextField("Notes", blank=True)
    url = models.URLField("URL", unique=True)
    #can add category but we won't for now
    #created_at and last_modified fields are very useful for almost any project
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

