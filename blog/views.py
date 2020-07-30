from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *
# Create your views here.

class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

