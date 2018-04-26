from django.db import models


class Post(models.Model):
    userId = models.IntergerField(default=1)
    title = models.CharField(default="Default Title", max_length = 200)
    body = models.TextField(default-"Body of post goes here")
    picture = models.ImageField(default = "default.png")