from django.shortcuts import render
from .models import Bookmark

def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'bookmarks': Bookmark.objects.all()}
    return render(request, 'bookmarks/index.html', context)


# Create your views here.
