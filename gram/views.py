from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import GramLetterForm
from .email import send_welcome_email
# Create your views here.
def welcome(request):
   return render(request, 'welcome.html')

def gram_today(request):
    if request.method == 'POST':
        form = GramLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = GramLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('gram_today')
            #.................
    return render(request, 'all-gram/today-gram.html', {gram":gram,"letterForm":form})