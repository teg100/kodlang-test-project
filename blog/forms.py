from django.forms import ModelForm
from django import forms
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ()
        widgets = {
            'title': forms.TextInput(attrs={"class": 'input-post-title',
                                            'placeholder': 'Введите название статьи'}),
            'image': forms.FileInput(attrs={"id": 'img'})
        }