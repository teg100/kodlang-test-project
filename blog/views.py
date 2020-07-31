from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from .models import *
from .forms import *
# Create your views here.

class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()[1:10]

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.first()
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('posts_list_url')
