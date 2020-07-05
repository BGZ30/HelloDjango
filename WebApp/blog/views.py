from django.shortcuts import render
from django.views.generic import ListView, DetailView
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

    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order posts by date desc

class PostDetailView(DetailView):
    model = Post  

# hAbout page
def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})