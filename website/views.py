from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse


def index_page(request):
    return render(request, "web/index.html")


def about_page(request):
    return render(request, "web/about.html")


def contact_us(request):
    return render(request, "web/contact.html")
