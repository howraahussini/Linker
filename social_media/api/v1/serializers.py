from rest_framework import serializers

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


class EmailSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Email.
    '''
    
    class Meta:
        model = Email
        fields = '__all__'
        
        
class PhoneSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Phone.
    '''
    
    class Meta:
        model = Phone
        fields = '__all__'
        
        
        
class InstagramSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Instagram.
    '''
    
    class Meta:
        model = Instagram
        fields = '__all__'
        
        
class TelegramSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Telegram.
    '''
    
    class Meta:
        model = Telegram
        fields = '__all__'
        
        
class YoutubeSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Youtube.
    '''
    
    class Meta:
        model = Youtube
        fields = '__all__'
        
        
class WhatsappSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Whatsapp.
    '''
    
    class Meta:
        model = Whatsapp
        fields = '__all__'
        
        
        
class XSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing X.
    '''
    
    class Meta:
        model = X
        fields = '__all__'
        
        
        
class FacebookSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Facebook.
    '''
    
    class Meta:
        model = Facebook
        fields = '__all__'
        
        
class LinkedinSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Linkedin.
    '''
    
    class Meta:
        model = Linkedin
        fields = '__all__'
        
        
class SnapchatSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Snapchat.
    '''
    
    class Meta:
        model = Snapchat
        fields = '__all__'
        
        
class TiktokSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Tiktok.
    '''
    
    class Meta:
        model = Tiktok
        fields = '__all__'