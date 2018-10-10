from django.http import HttpResponse
from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Profile , Image, Comment
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm


# Create your views here.
# def welcome(request):
#     images = Image.objects.all()

#     context = {
#         'images':images , 
#     }
#     return render(request, 'welcome.html', {"images":images})


@login_required(login_url='/login')
def welcome(request):
    images = Image.objects.all()
    print(images)
    return render(request,'welcome.html',{"images":images})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-gram/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "no term matches your search"
        return render(request, 'all-gram/search.html',{"message":message})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        image_form = NewImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        image_form = NewImageForm()
    return render(request, 'new_image.html', {"image_form": image_form})


@login_required(login_url='/accounts/login/')
def profile(request, user_username = None):
    if user_username == None:
        user = request.user
    else:
        user = get_object_or_404( User ,username = user_username)
    
    profile = Profile.get_user_profile( user )
    title = "Profile"
    images = Image.get_image_by_id(user.id)
    print(images)

    context = {
        'title':title, 
        "images":images,
        "profile" : profile }
        
    return render(request, 'profile/profile.html',context)



@login_required(login_url='/accounts/login/')
def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        name = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=name)
        message = f"{name}"
        profiles = User.objects.all()
        print(profiles)
        return render(request, 'search.html', {"message":message, "usernames":searched_profiles, "profiles":profiles,})