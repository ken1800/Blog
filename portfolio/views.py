from django.shortcuts import render,redirect
from . import models
from .forms import ContactForm
from django.contrib import messages

def index(request):
    home = models.Home.objects.order_by("-id")[:1]
    Text = models.TextHome.objects.all()
    work = models.Work.objects.all()
    
   # news = News.objects.order_by("-date")[:10]
    return render(request, 'index.html',{"home": home,"Text":Text,"work":work,})
def about(request):
    about = models.About.objects.all()
    return render(request, 'about.html',{'about':about})
def contact(request):
    contact = models.Contact.objects.all()
    return render(request, 'contact.html',{ 'contact': contact })


# Create your views here.
