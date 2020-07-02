from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # to show a flash message
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        """ if the form is valid, info is stored in cleaned_data dicd"""
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}')

            return redirect('blog-home')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
