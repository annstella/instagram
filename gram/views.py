from django.shortcuts import render,redirect
# Create your views here.
def welcome(request):
   return render(request, 'all-gram/today-gram.html')

def gram(request):
   gram = Image.objects.all()

   return render(request, 'all-gram/today-gram.html', {"gram":gram})