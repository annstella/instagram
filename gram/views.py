from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile , Image

from .email import send_welcome_email
# Create your views here.
def welcome(request):
    images = Image.objects.all()

    context = {
        'images':images , 
    }
    return render(request, 'welcome.html', context)

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-gram/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "no term matches your search"
        return render(request, 'all-gram/search.html',{"message":message})

