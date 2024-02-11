from django_filters import rest_framework as filters
from panel.models import (
    Profile,
    Text,
    Link,
    Gallery,
    FAQUser
)

class ProfileFilter(filters.FilterSet):
    '''
    This is for filter profile by link_id .
    '''
    
    class Meta:
        model = Profile
        fields = {
            'link_id': [
                'exact',
            ],
        }
        
        
class TextFilter(filters.FilterSet):
    '''
    This is for filter text by link_id .
    '''
    
    class Meta:
        model = Text
        fields = {
            'link_id': [
                'exact',
            ],
        }

     
class LinkFilter(filters.FilterSet):
    '''
    This is for filter link by link_id .
    '''
    
    class Meta:
        model = Link
        fields = {
            'link_id': [
                'exact',
            ],
        }
        
        
class GalleryFilter(filters.FilterSet):
    '''
    This is for filter by gallery link_id .
    '''
    
    class Meta:
        model = Gallery
        fields = {
            'link_id': [
                'exact',
            ],
        }     
        
        
class FAQUserFilter(filters.FilterSet):
    '''
    This is for filter FAQUser by link_id .
    '''
    
    class Meta:
        model = FAQUser
        fields = {
            'link_id': [
                'exact',
            ],
        }