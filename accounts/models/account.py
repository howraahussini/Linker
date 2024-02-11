from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .users import User

class Account(models.Model):
    '''
    this is made for each user to hold their information.
    '''

    user = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='مستخدم')
    first_name = models.CharField(max_length=255, verbose_name='الإسم')
    last_name = models.CharField(max_length=255, verbose_name='اللقب')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __srt__(self):
        return self.user.email
    


@receiver(post_save, sender=User)
def save_account(sender, instance, created, **kwargs):
    '''
    A signal for a user's creation post that only activate when the user is created
    '''
    if created :
        Account.objects.create(user=instance)