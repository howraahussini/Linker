from django_filters import rest_framework as filters

from social_media.models import (
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


class EmailFilter(filters.FilterSet):
    '''
    This is for filter Email by link id .
    '''
    
    class Meta:
        model = Email
        fields = {
            "link_id": [
                "exact",
            ],
        }
             
        
class PhoneFilter(filters.FilterSet):
    '''
    This is for filter Phone by link id .
    '''
    
    class Meta:
        model = Phone
        fields = {
            "link_id": [
                "exact",
            ],
        }
              
        
class InstagramFilter(filters.FilterSet):
    '''
    This is for filter Instagram by link id .
    '''
    
    class Meta:
        model = Instagram
        fields = {
            "link_id": [
                "exact",
            ],
        }
             
        
class TelegramFilter(filters.FilterSet):
    '''
    This is for filter Telegram by link id .
    '''
    
    class Meta:
        model = Telegram
        fields = {
            "link_id": [
                "exact",
            ],
        }
        
             
class YoutubeFilter(filters.FilterSet):
    '''
    This is for filter Youtube by link id .
    '''
    
    class Meta:
        model = Youtube
        fields = {
            "link_id": [
                "exact",
            ],
        }
              
        
class WhatsappFilter(filters.FilterSet):
    '''
    This is for filter Whatsapp by link id .
    '''
    
    class Meta:
        model = Whatsapp
        fields = {
            "link_id": [
                "exact",
            ],
        }      
        
        
class XFilter(filters.FilterSet):
    '''
    This is for filter X by link id .
    '''
    
    class Meta:
        model = X
        fields = {
            "link_id": [
                "exact",
            ],
        }
        
        
class FacebookFilter(filters.FilterSet):
    '''
    This is for filter Facebook by link id .
    '''
    
    class Meta:
        model = Facebook
        fields = {
            "link_id": [
                "exact",
            ],
        }      
        
        
class LinkedinFilter(filters.FilterSet):
    '''
    This is for filter Linkedin by link id .
    '''
    
    class Meta:
        model = Linkedin
        fields = {
            "link_id": [
                "exact",
            ],
        }        
        
        
class SnapchatFilter(filters.FilterSet):
    '''
    This is for filter Snapchat by link id .
    '''
    
    class Meta:
        model = Snapchat
        fields = {
            "link_id": [
                "exact",
            ],
        }
        
               
class TiktokFilter(filters.FilterSet):
    '''
    This is for filter Tiktok by link id .
    '''
    
    class Meta:
        model = Tiktok
        fields = {
            "link_id": [
                "exact",
            ],
        }
