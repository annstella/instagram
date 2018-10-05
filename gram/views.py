from django.shortcuts import render,redirect
from .forms import NewsLetterForm
# Create your views here.
def welcome(request):
   return render(request, 'welcome.html')

def gram_today(request):
#........
    if request.method == 'POST':
        form = GramLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = GramLetterForm()
    return render(request, 'all-gram/today-gram.html', {gram":gram,"letterForm":form})