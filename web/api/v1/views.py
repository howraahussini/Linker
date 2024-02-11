from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from accounts.api.v1.pagination import Pagination

from ...models import Contact, FAQ

from .serializers import ContactSerializer, FAQSerializer


class ContactModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Contacts.
    Can only be done by superuser.
    '''
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ['name', 'email', 'subject', 'message']
    pagination_class = Pagination


class FAQModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting FAQs.
    Can only be done by superuser.
    '''
    
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ['question', 'answer']
    pagination_class = Pagination