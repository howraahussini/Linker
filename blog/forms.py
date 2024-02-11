from django import forms
from captcha.fields import CaptchaField

from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    this is for comments model.
    '''
    
    captcha = CaptchaField()
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
