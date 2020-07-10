from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

""" Each class is gonna be its own table in the database 
    and each atterbiute is a field in that table."""

# Post table
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kw)