from django.contrib import admin
from .models import (
    Link,
    Profile,
    Text,
    Gallery,
    FAQUser
)

class LinkAdmin(admin.ModelAdmin):
    '''
    this is for managing links.
    '''

    model = Link
    list_display = ('title', 'link_id', 'created_date', 'updated_date')
    search_fields = ('title', 'link')
    list_filter = ('created_date', 'link_id')



class ProfileAdmin(admin.ModelAdmin):
    '''
    this is for managing profile.
    '''

    model = Profile
    list_display = ('username', 'link_id', 'created_date', 'updated_date')
    search_fields = ('username', 'biography')
    list_filter = ('created_date', 'link_id')


class TextAdmin(admin.ModelAdmin):
    '''
    this is for managing text.
    '''

    model = Text
    list_display = ('link_id', 'created_date', 'updated_date')
    search_fields = ('text',)
    list_filter = ('created_date', 'link_id')


class GalleryAdmin(admin.ModelAdmin):
    '''
    this is for managing Gallery.
    '''

    model = Gallery
    list_display = ('link_id', 'created_date', 'updated_date')
    search_fields = ('caption',)
    list_filter = ('created_date', 'link_id')




class FAQUserAdmin(admin.ModelAdmin):
    '''
    this is for managing main links.
    '''

    model = FAQUser
    list_display = ('link_id', 'created_date', 'updated_date')
    search_fields = ('question', 'answer')
    list_filter = ('created_date', 'link_id')



# registration model in admin panel

admin.site.register(Link, LinkAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(FAQUser, FAQUserAdmin)