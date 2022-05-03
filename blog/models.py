from django.db import models

# Create your models here.

class ContactFormModel(models.Model):
    name = models.CharField(max_length=20, help_text="Enter your name.")
    date_now = models.DateTimeField(auto_now_add=True)

   
