from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images/")
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

