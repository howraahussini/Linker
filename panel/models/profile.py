from django.db import models
from dashboard.models import MainLink
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    '''
    this is a profile for the main link.
    '''

    link_id = models.ForeignKey(MainLink, on_delete= models.CASCADE)
    username = models.CharField(max_length=255, verbose_name='اسم المستخدم')
    image = models.ImageField(default='user/logo.svg', upload_to='user/', verbose_name='صورة')
    biography = models.TextField(verbose_name='سيرة شخصية')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.username

@receiver(post_save, sender=MainLink)
def save_profile(sender, instance, created, **kwargs):
    '''
    A signal for a user's creation post that only activate when the user is created.
    '''
    if created :
        Profile.objects.create(link_id=instance)