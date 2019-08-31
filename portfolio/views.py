from django.shortcuts import render
from . import models

def index(request):
    home = models.Home.objects.all()
    
    return render(request, 'index.html',{"home": home})
def about(request):
    return render(request, 'about.html',{})
def contact(request):
    return render(request, 'contact.html',{})


# Create your views here.
