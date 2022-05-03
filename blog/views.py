from django.shortcuts import render
from blog.models import ContactFormModel
from blog.forms import ContactForm

# Create your views here.

def index(request):
    names = ContactFormModel.objects.all()
    context = {
        'names': names
    }

    return render(request, "blog/index.html", context=context)