from django import forms
from django.utils.translation import ugettext as _

from .models import MainLink


class MainLinkForm(forms.ModelForm):
    '''
    this is a form for creating main links by user.
    '''

    error_messages = _('the name must be unique')

    text_help = _('Your name can contain numbers, English letters, dots and dashes')

    class Meta:
        model = MainLink
        fields = ['name',]