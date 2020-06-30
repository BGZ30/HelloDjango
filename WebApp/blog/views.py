from django.shortcuts import render

#HTTP response
from django.http import HttpResponse

# handle the traffic

# Home page
def home(requset):
    return HttpResponse('<h1>Blog home</h1>')

# hAbout page
def about(requset):
    return HttpResponse('<h1>Blog about</h1>')
