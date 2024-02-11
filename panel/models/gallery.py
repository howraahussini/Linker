from django.db import models
from dashboard.models import MainLink


class Gallery(models.Model):
    '''
    this is a gallery for the main link.
    '''

    link_id = models.ForeignKey(MainLink, on_delete= models.CASCADE)
    image = models.ImageField(default='user/logo.svg', upload_to='gallery/', verbose_name='صورة')
    caption = models.TextField(verbose_name='شرح', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.caption