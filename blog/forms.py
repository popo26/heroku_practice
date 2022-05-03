import datetime

from django.forms import ModelForm, ValidationError
from blog.models import ContactFormModel

class ContactForm(ModelForm):
    
    class Meta:
        model = ContactFormModel
        fields = ['name']
        


