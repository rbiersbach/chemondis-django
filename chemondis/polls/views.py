from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. It is now " + datetime.datetime.now().strftime('%H:%M:%S'))
