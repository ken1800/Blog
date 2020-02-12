from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

#from . import views
class Home(models.Model):
    topic =models.CharField(max_length=200)
    information = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.topic
    
class TextHome(models.Model):
    text1_h =models.CharField(max_length=200,default="")
    text1 = models.TextField(max_length=400) 
    text2_h =models.CharField(max_length=200,default="")  
    text2 = models.TextField(max_length=500)
    
    def __str__(self):
        return self.text1
    
class Contact(models.Model):
    
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    number = models.IntegerField()
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    
    def __str__(self):
            return self.name
        
class Work(models.Model):
    title = models.CharField(max_length=100)
    text =  models.TextField(max_length=600)
    link =  models.CharField(max_length=100)
    
    def __str__(self):
            return self.title
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
    
# class ProfileFeedItem(models.Model):
#     """Profile status update"""
#     user_profile = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     status_text = models.CharField(max_length=255)
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """Return the model as a string"""
#         return self.status_text

class About(models.Model):
    """ I exposed this model to the api and anyone who is authenticated can be able to edit or post in the about page """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    
    def __str__(self):
        return self.text
    
    
    
    
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title