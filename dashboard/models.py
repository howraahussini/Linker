from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from accounts.models import Account


class MainLink(models.Model):
    '''
    This is the MainLink.
    '''

    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='الموجد')
    name = models.CharField(max_length=255, unique=True, verbose_name='الإسم')
    template = models.ForeignKey('MainLinkTemplate', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='لون القالب')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.author.user.email



class MainLinkTemplate(models.Model):
    ''' 
    This is for template field in MainLink and determines the theme off the page.
    This is to limit the file size to 10 MB.
    '''

    template_name = models.CharField(default='theme',max_length=150 ,unique=True ,verbose_name='اسم القالب')
    background = models.ImageField(upload_to='background/', verbose_name='خلفیه') # limit file size to 10MB
    profile_block = models.CharField(default='#eaf9f3', max_length=20, verbose_name='لون ملف التعريف',  help_text= (_('Make sure to put a "#'' before color code')))
    url_block = models.CharField(default='#6dafa7', max_length=20, verbose_name= 'لون روابط', help_text= (_('Make sure to put a "#'' before color code')))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')
    
    def __str__(self):
        return self.template_name


@receiver(post_save, sender=Account)
def save_main_link(sender, instance, created, **kwargs):
    '''
    A signal for a user's creation post that only activate when the user is created.
    '''
    if created :
        MainLink.objects.create(author=instance, name='Linker')


