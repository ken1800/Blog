from django.db import models
from . import views
class Home(models.Model):
    topic =models.CharField(max_length=200)
    information = models.TextField(max_length=600)

    def __str__(self):
        return self.topic+"-"+str(self.information)
    
    

# Create your models here.
