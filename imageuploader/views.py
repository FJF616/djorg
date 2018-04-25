from django.shortcuts import render
from imageuploader.models import Uploader, UploadForm
from django.http import HttpResponseRedirectfrom 
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:   
        img=UploadForm()
    images=Uploader.objects.all()
    return render(request, 'home.html', {'form':img, 'images':images})
