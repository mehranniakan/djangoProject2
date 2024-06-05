from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import json
from website.forms import ContactForm
from website.models import Contact


# Create your views here.

def index_page(request):
    return render(request, "web/index.html")


def about_page(request):
    return render(request, "web/about.html")


class CaptchaTestForm:
    pass


def contact_us(request):
    contact_form = ContactForm(request)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            if not bool(contact_form.data.get('Subject')):
                contact_form.instance.Subject = None
            contact_form.instance.Name = "Unknown"
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "You're Request has Successfuly Submitted !")
        else:
            print(contact_form.errors)
            messages.add_message(request, messages.ERROR, "You're Request has not Submitted !")
    elif request.method == 'GET':
        print('Get Method')
    else:
        print('Invalid Method')
    return render(request, "web/contact.html", {'form': contact_form})
