from django.shortcuts import render

#HTTP response
from django.http import HttpResponse

# handle the traffic
def home(requset):
    return HttpResponse('<h1>Blog home</h1>')

