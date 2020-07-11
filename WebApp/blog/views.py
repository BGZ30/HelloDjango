from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # go to the homepage

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# hAbout page
def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})