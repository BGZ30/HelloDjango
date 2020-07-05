from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # specify the model that this form is gonna interact with
    class Meta:
        # if the form is valid, then it will create a user
        model = User

        # fields shown on the form
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # specify the model that this form is gonna interact with
    class Meta:
        # if the form is valid, then it will create a user
        model = User

        # fields shown on the form
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
