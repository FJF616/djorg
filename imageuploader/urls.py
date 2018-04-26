from django.urls import path
from . import views


urlpatterns = [
    path('', views.SaveProfile, name='SaveProfile'),
   
]