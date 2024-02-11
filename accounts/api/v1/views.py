from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import Pagination
from .serializers import AccountSerializer
from ...models import Account



class AccountModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting accounts
    Can only be done by superuser.
    '''
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ['user', 'first_name',  'last_name']
    pagination_class = Pagination
    