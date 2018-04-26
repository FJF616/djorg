from django.shortcuts import render
from django.http import HttpResponseRedirectfrom 
from django.urls import reverse


class PostSerializer(serializers.HyperlinkedModelSErializer):
    class Meta: 
        model = PostSerializerfields = ("userId", "id", "title", "picture")