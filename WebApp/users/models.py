from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    One to one relationship between user and profile; one user has one profile
    CASCADE: if the user is deleted--> delete the profile "BUT" if the profile is deleted DON'T delete the user 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 
