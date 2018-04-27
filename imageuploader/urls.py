from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('imageuploader/', TemplateView.as_view(template_name='index.html'))  
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)