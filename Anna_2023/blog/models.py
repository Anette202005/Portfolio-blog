from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

