from django.db import models

# Create your models here.


class Contact(models.Model):
    '''
    This model is for contact form to send feedback by user.
    '''
    
    name = models.CharField(max_length=150, verbose_name='اسم')
    email = models.EmailField(verbose_name='ايميل')
    subject = models.CharField(max_length=250, verbose_name='الموضوع')
    message = models.TextField(verbose_name='الرسالة')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.name
    

class FAQ(models.Model):
    '''
    this is a FAQUer model for answer FAQ question.
    '''

    question = models.TextField(verbose_name='سؤال')
    answer = models.TextField(verbose_name='جواب')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.question