
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        #from . import models
       # model = models.Contact
        fields =['names','email','number','subject','text']

