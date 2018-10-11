from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image, Comment

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'post']


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['creator', 'likes', 'time', 'comment', 'profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['time','likes']
#         fields = ['image','caption']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption']
