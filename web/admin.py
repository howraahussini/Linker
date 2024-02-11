from django.contrib import admin

from .models import Contact, FAQ


class ContactAdmin(admin.ModelAdmin):
    '''
    this is for managing contact.
    '''

    model = Contact
    list_display = ('name', 'subject', 'created_date', 'updated_date')
    search_fields = ('name', 'subject', 'message')
    list_filter = ('created_date', )


class FAQAdmin(admin.ModelAdmin):
    '''
    this is for managing FAQ.
    '''

    model = FAQ
    list_display = ('question', 'created_date', 'updated_date')
    search_fields = ('question', 'answer')
    list_filter = ('created_date',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(FAQ, FAQAdmin)