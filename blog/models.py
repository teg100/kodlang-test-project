from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images/")
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'pk': self.id})

    def __str__(self):
        return self.title

