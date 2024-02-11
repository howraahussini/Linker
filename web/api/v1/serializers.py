from rest_framework import serializers

from ...models import Contact, FAQ


class ContactSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing Contact.
    '''
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class FAQSerializer(serializers.ModelSerializer):
    '''
    this class is for serializing FAQ.
    '''
    
    class Meta:
        model = FAQ
        fields = '__all__'