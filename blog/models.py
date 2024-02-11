from django.db import models

from accounts.models import Account


class Category(models.Model):
    """
    this class is for blog posts categories
    """

    name = models.CharField(max_length=255, verbose_name='فئة')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    this class is for blog posts
    """

    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/',null=True, blank=True, verbose_name='صورة')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوى')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='فئة')
    status = models.BooleanField(default=False, verbose_name='الحالة')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')
    published_date = models.DateTimeField(verbose_name='تاريخ النشر')

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    '''
    This is a post's comment.
    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='اسم')
    email = models.EmailField(verbose_name='ايميل')
    message = models.TextField(verbose_name='الرساله')
    approved = models.BooleanField(default=False, verbose_name='موافقة')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    def __str__(self):
        return self.name