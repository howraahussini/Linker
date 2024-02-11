from django.db import models
from dashboard.models import MainLink


class FAQUser(models.Model):
    '''
    this is a FAQUser for the main link.
    '''

    link_id = models.ForeignKey(MainLink, on_delete= models.CASCADE)
    question = models.TextField(verbose_name='سؤال')
    answer = models.TextField(verbose_name='جواب')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.question