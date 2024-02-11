from rest_framework import serializers

from ...models import Account


class AccountSerializer(serializers.ModelSerializer):
    '''
    this is for serializing user Accounts.
    '''
    
    class Meta:
        model = Account 
        fields = '__all__'
        
        
        