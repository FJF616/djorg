from django.contrib import admin
from .models import Bookmark
# Register your models here.
from .models import Note
# Register your models here.

admin.site.register(Note)

admin.site.register(Bookmark)
