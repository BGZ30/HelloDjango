from django.shortcuts import render

#HTTP response
from django.http import HttpResponse

# handle the traffic

# Home page
def home(request):
    # return HttpResponse('<h1>Blog home</h1>')
    return render(request, 'blog/home.html')

# hAbout page
def about(request):
    return HttpResponse('<h1>Blog about</h1>')
