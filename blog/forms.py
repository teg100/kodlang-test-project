from django.forms import ModelForm
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ()