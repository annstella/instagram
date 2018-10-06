from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image

from .email import send_welcome_email
# Create your views here.
def welcome(request):
   return render(request, 'welcome.html')

