from django.shortcuts import render,redirect
from . import models
from .forms import ContactForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from portfolio import permissions
from rest_framework import filters,generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

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


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.About.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
   
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
    
class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
   
class NoteList(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
  