from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from accounts.api.v1.pagination import Pagination

from ...models import MainLink, MainLinkTemplate
from .filters import MainLinkFilter
from .serializers import MainLinkSerializer, MainLinkTemplateSerializer


class MainLinkModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting MainLinks.
    Can only be done by superuser.
    '''
    
    queryset = MainLink.objects.all()
    serializer_class = MainLinkSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MainLinkFilter
    search_field = ['author', 'name', 'template']
    pagination_class = Pagination
    
    
class MainLinkTemplateModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting MainLinkTemplates.
    Can only be done by superuser.
    '''
    
    queryset = MainLinkTemplate.objects.all()
    serializer_class = MainLinkTemplateSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ['author', 'name', 'template']
    pagination_class = Pagination
    

