from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile/')

    def __str__(self):
       return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profile(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()
   

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    user= models.ForeignKey(User)
    # post = HTMLField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    def save_images(self):
        self.save()

    def total_likes(self):
        return self.likes.count()

    def save_comment(self):
        self.save()


class Comment(models.Model):
    text = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    time_posted = models.DateTimeField(auto_now_add=True)



    def save_comment(self):
        self.save()

    def __str__(self):
        return self.text


class Follow(models.Model):
    follower = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def follow(cls, current_user, new_follow):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.follower.add(new_follow)

    @classmethod
    def unfollow(cls, current_user, new_follow):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.follower.remove(new_follow)


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()