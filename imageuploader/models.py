from django.db import models
from django.forms import ModelForm
 
# Create your models here.
class Uploader(models.Model):
    pic = models.FIleField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)

#Form model
class UploadForm(ModelForm):
    class Meta:
        model = Uploaderfields = ('pic',)