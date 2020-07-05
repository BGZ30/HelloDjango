from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # to show a flash message
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        """ if the form is valid, info is stored in cleaned_data dicd"""
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login.')

            return redirect('login')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    # Create the forms
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    # pass them to the template, first create a context, then pass it to the template
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    # pass the context to be able to access it 
    return render(request, 'users/profile.html', context)

