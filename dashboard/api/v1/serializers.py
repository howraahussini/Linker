from rest_framework import serializers

from ...models import MainLink, MainLinkTemplate


class MainLinkSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing MainLink.
    '''
    
    class Meta:
        model = MainLink
        fields = '__all__'
        
        
        
class MainLinkTemplateSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing MainLinkTemplate.
    '''
    
    class Meta:
        model = MainLinkTemplate
        fields = '__all__'