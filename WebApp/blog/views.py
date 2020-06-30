from django.shortcuts import render

#HTTP response
# from django.http import HttpResponse

# handle the traffic

# Adding some dummy data
posts = [
    {
        'author': 'Bassant',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 30, 2020'
    },
    {
        'author': 'Maisa',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 30, 2020'
    }
]

# Home page
def home(request):

    """ pass the data to the template;
        create a dictionary with a key called posts, and values are the dummy data 'posts'
    """
    context = {'posts': posts}

    # return HttpResponse('<h1>Blog home</h1>')
    return render(request, 'blog/home.html', context)

# hAbout page
def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html')