#using django to handle creating users and login validation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# create models for user and and fields they should fill in the form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")