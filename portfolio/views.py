from django.shortcuts import render
from . import models

def index(request):
    home = models.Home.objects.order_by("-id")[:1]
    Text = models.TextHome.objects.all()
    
   # news = News.objects.order_by("-date")[:10]
    return render(request, 'index.html',{"home": home,"Text":Text,})
def about(request):
    return render(request, 'about.html',{})
def contact(request):
    return render(request, 'contact.html',{})


# Create your views here.
