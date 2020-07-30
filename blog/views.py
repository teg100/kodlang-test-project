from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
# Create your views here.


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

