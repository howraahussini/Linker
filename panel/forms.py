from django import forms
from .models import (
    Link,
    Profile,
    Text,
    Gallery,
    FAQUser
)
from dashboard.models import MainLink


class LinkForm(forms.ModelForm):
    '''
    this is a form for link model.
    '''

    class Meta:
        model = Link
        fields = ['link', 'title']
        

class ProfileForm(forms.ModelForm):
    '''
    this is a form for Profile model.
    '''

    class Meta:
        model = Profile
        fields = ['username', 'image', 'biography']


class TextForm(forms.ModelForm):
    '''
    this is a form for Text model.
    '''

    class Meta:
        model = Text
        fields = ['text']

class GalleryForm(forms.ModelForm):
    '''
    this is a form for Gallery model.
    '''

    class Meta:
        model = Gallery
        fields = ['image', 'caption']


class FAQUserForm(forms.ModelForm):
    '''
    this is a form for FAQUser model.
    '''

    class Meta:
        model = FAQUser
        fields = ['question', 'answer',]


class MainLinkTemplateForm(forms.ModelForm):
    '''
    this is for main_link_template form .
    '''
    
    class Meta:
        model = MainLink
        fields = ['template', ]