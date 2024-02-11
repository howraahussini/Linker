from django.db import models
from dashboard.models import MainLink


class Phone(models.Model):
    '''
    This is to create a Phone link for the main link.
    '''      
    
    link_id = models.ForeignKey(MainLink, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='عنوان')
    number = models.IntegerField(max_length=15, verbose_name='رقم الهاتف')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self) :
        return self.title