from django.db import models


class Profile(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField(default="Default Title", max_length = 200)
    body = models.TextField(defaul="Body of post goes here")
    picture = models.ImageField(default = "default.png")

    class Meta: 
        db_table = "profile"