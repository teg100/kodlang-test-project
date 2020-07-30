from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images/")
    text = models.TextField()


    def __str__(self):
        return self.title

