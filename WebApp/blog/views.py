from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

#HTTP response
# from django.http import HttpResponse

# handle the traffic

# Home page
def home(request):

    """ pass the data to the template;
        create a dictionary with a key called posts, and values are the dummy data 'posts'
    """
    context = {'posts': Post.objects.all()}

    # return HttpResponse('<h1>Blog home</h1>')
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post


# hAbout page
def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})