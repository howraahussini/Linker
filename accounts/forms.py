from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Account, User


class SignUpForm(UserCreationForm):
    '''
    this is a form for signup users with email and password.
    '''

    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    '''
    this is a form for login users with email and password.
    '''

    captcha = CaptchaField()

    class Meta:
        model = User
        fields =  ['email', 'password']


class AccountForm(forms.ModelForm):
    '''
    this is a form for displaying user information.
    '''

    class Meta:
        model = Account
        fields = ['first_name', 'last_name']