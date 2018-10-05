from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   bio = models.CharField(max_length=200)
   profile_pic = models.ImageField(upload_to='profile/')

    def __str__(self):
       return self.first_name
   

class Image(models.Model):
   image = models.ImageField(upload_to='images/')
   caption = models.TextField(blank=True)
   likes = models.PositiveIntegerField(default=0)
   comment = models.CharField(max_length=200)
   profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
