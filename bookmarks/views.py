from django.shortcuts import render
from .models import Bookmark

def index(request):
    context = {'bookmarks': Bookmark.objects.all()}
    return render(request, 'bookmarks/index.html', context)


# Create your views here.
