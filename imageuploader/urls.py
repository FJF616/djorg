from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
   'myapp.views', url(r'^profile/',TemplateView.as_view(
      template_name = 'profile.html')), url(r'^saved/', 'SaveProfile', name = 'saved')
)