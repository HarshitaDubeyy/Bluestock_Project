from django import forms
import django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


    

