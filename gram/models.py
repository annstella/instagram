from django.db import models

# Create your models here.
class Image(models.Model):
   image = models.ImageField(upload_to='images/')
   caption = models.TextField(blank=True)
   likes = models.PositiveIntegerField(default=0)
   comment = models.CharField(max_length=200)
   profile = models.ForeignKey(profile, on_delete=models.CASCADE)
