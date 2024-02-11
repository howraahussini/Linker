from django.contrib import admin
from .models import (
    Email,
    Phone,
    Instagram,
    Telegram,
    Youtube,
    Whatsapp,
    X,
    Facebook,
    Linkedin,
    Snapchat,
    Tiktok
)


class PhoneAdmin(admin.ModelAdmin):
    '''
    this is for managing Phone.
    '''

    model = Phone
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'number')
    list_filter = ('created_date', 'link_id')


class EmailAdmin(admin.ModelAdmin):
    '''
    this is for managing Email.
    '''

    model = Email
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'email')
    list_filter = ('created_date', 'link_id')


class InstagramAdmin(admin.ModelAdmin):
    '''
    this is for managing Instagram.
    '''

    model = Instagram
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class TelegramAdmin(admin.ModelAdmin):
    '''
    this is for managing Telegram.
    '''

    model = Telegram
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class YoutubeAdmin(admin.ModelAdmin):
    '''
    this is for managing Youtube.
    '''

    model = Youtube
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class WhatsappAdmin(admin.ModelAdmin):
    '''
    this is for managing Whatsapp.
    '''

    model = Whatsapp
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class XAdmin(admin.ModelAdmin):
    '''
    this is for managing X.
    '''

    model = X
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class FacebookAdmin(admin.ModelAdmin):
    '''
    this is for managing Facebook.
    '''

    model = Facebook
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class LinkedinAdmin(admin.ModelAdmin):
    '''
    this is for managing Linkedin.
    '''

    model = Linkedin
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class SnapchatAdmin(admin.ModelAdmin):
    '''
    this is for managing Snapchat.
    '''

    model = Snapchat
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')


class TiktokAdmin(admin.ModelAdmin):
    '''
    this is for managing Tiktok.
    '''

    model = Tiktok
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')



# registration model in admin panel

admin.site.register(Phone, PhoneAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Instagram, InstagramAdmin)
admin.site.register(Telegram, TelegramAdmin)
admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(Whatsapp, WhatsappAdmin)
admin.site.register(X, XAdmin)
admin.site.register(Facebook, FacebookAdmin)
admin.site.register(Linkedin, LinkedinAdmin)
admin.site.register(Snapchat, SnapchatAdmin)
admin.site.register(Tiktok, TiktokAdmin)