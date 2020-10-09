from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    firstname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    native_language = models.CharField(max_length=30)
    also_speaks = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    created_with = models.DateTimeField(auto_now=True)
    intro_video = models.CharField(max_length=11)
    image = models.ImageField(default='default.png',upload_to='profile_pics')



    def __str__(self):
    	return f'{self.user.username} profile'