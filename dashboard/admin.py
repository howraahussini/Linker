from django.contrib import admin

from .models import MainLink, MainLinkTemplate


class MainLinkAdmin(admin.ModelAdmin):
    '''
    this is for managing main links.
    '''

    model = MainLink
    list_display = ('name', 'id', 'template', 'created_date', 'updated_date')
    search_fields = ('name',)
    list_filter = ('created_date',)


class MainLinkTemplateAdmin(admin.ModelAdmin):
    '''
    this is for managing template main link.
    '''

    model = MainLinkTemplate
    list_display = ('template_name', 'created_date', 'updated_date')
    search_fields = ('template_name',)
    list_filter = ('template_name',)

admin.site.register(MainLink, MainLinkAdmin)    
admin.site.register(MainLinkTemplate, MainLinkTemplateAdmin)    