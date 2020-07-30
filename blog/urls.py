from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:pk>/', PostView.as_view(), name='post_detail_url')
]