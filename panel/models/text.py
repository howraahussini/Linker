from django.db import models

from dashboard.models import MainLink


class Text(models.Model):
    '''
    this is a text created for the main link.
    '''

    link_id = models.ForeignKey(MainLink, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='نص', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.text