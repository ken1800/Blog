from django.db import models
from . import views
class Home(models.Model):
    topic =models.CharField(max_length=200)
    information = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.topic+"-"+str(self.information)
    
class TextHome(models.Model):
    text1 = models.TextField(max_length=400)  
    text2 = models.TextField(max_length=500)

# Create your models here.
