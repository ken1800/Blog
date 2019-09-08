from django.db import models
from . import views
class Home(models.Model):
    topic =models.CharField(max_length=200)
    information = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.topic+"-"+str(self.information)
    
class TextHome(models.Model):
    text1_h =models.CharField(max_length=200,default="")
    text1 = models.TextField(max_length=400) 
    text2_h =models.CharField(max_length=200,default="")  
    text2 = models.TextField(max_length=500)
    
    def __str__(self):
        return self.text1+"-"+str(self.text1_h)
    
class About(models.Model):
    Title = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    
    def __str__(self):
        return self.text+"-"+str(self.Title)
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    number = models.IntegerField(max_length=13)
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    

# Create your models here.
