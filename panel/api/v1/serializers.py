from rest_framework import serializers
from panel.models import (
    Profile,
    Text,
    Link,
    Gallery,
    FAQUser
)

class ProfileSerializer(serializers.ModelSerializer):
    '''
    This class is for serializing profile.
    '''
    
    class Meta:
        model = Profile
        fields = '__all__'
        

class TextSerializer(serializers.ModelSerializer):
    '''
    This class is for serializing Text.
    '''
    
    class Meta:
        model = Text
        fields = '__all__'
        
        
        
class LinkSerializer(serializers.ModelSerializer):
    '''
    This class is for serializing Link.
    '''
    
    class Meta:
        model = Link
        fields = '__all__'
        
        
class GallerySerializer(serializers.ModelSerializer):
    '''
    This class is for serializing Gallery.
    '''
    
    class Meta:
        model = Gallery
        fields = '__all__'
        
        
        
class FAQUserSerializer(serializers.ModelSerializer):
    '''
    This class is for serializing FAQUser.
    '''
    
    class Meta:
        model = FAQUser
        fields = '__all__'