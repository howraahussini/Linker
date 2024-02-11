from django import forms
from .models import (
    Email,
    Phone,
    Instagram,
    Telegram,
    Youtube,
    Whatsapp,
    X,
    Facebook,
    Linkedin,
    Snapchat,
    Tiktok
)

class EmailForm(forms.ModelForm):
    '''
    this is a form for Email model.
    '''

    class Meta:
        model = Email
        fields = ['email', 'title']
 

class PhoneForm(forms.ModelForm):
    '''
    this is a form for Phone model.
    '''

    class Meta:
        model = Phone
        fields = ['number', 'title']


class InstagramForm(forms.ModelForm):
    '''
    this is a form for Instagram model.
    '''

    class Meta:
        model = Instagram
        fields = ['link', 'title']


class TelegramForm(forms.ModelForm):
    '''
    this is a form for Telegram model.
    '''

    class Meta:
        model = Telegram
        fields = ['link', 'title']


class YoutubeForm(forms.ModelForm):
    '''
    this is a form for Youtube model.
    '''

    class Meta:
        model = Youtube
        fields = ['link', 'title']


class WhatsappForm(forms.ModelForm):
    '''
    this is a form for Whatsapp model.
    '''

    class Meta:
        model = Whatsapp
        fields = ['link', 'title']


class XForm(forms.ModelForm):
    '''
    this is a form for X model.
    '''

    class Meta:
        model = X
        fields = ['link', 'title']

    
class FacebookForm(forms.ModelForm):
    '''
    this is a form for Facebook model.
    '''

    class Meta:
        model = Facebook
        fields = ['link', 'title']


class LinkedinForm(forms.ModelForm):
    '''
    this is a form for Linkedin model.
    '''

    class Meta:
        model = Linkedin
        fields = ['link', 'title']


class SnapchatForm(forms.ModelForm):
    '''
    this is a form for Snapchat model.
    '''

    class Meta:
        model = Snapchat
        fields = ['link', 'title']


class TiktokForm(forms.ModelForm):
    '''
    this is a form for Tiktok model.
    '''

    class Meta:
        model = Tiktok
        fields = ['link', 'title']