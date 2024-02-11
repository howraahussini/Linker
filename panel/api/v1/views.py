from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from accounts.api.v1.pagination import Pagination

from .filters import (
    ProfileFilter,
    TextFilter,
    LinkFilter,
    GalleryFilter,
    FAQUserFilter
)

from panel.models import (
    Profile,
    Text,
    Link,
    Gallery,
    FAQUser
)
from .serializers import (
    ProfileSerializer,
    TextSerializer,
    LinkSerializer,
    GallerySerializer,
    FAQUserSerializer     
)


class ProfileModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Profiles.
    Can only be done by superuser.
    '''
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProfileFilter
    search_field = ['link_id', 'username', 'biography']
    pagination_class = Pagination
    
    
    
class TextModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Texts.
    Can only be done by superuser.
    '''
    
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TextFilter
    search_field = ['link_id', 'text']
    pagination_class = Pagination
    

class LinkModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Links.
    Can only be done by superuser.
    '''
    
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LinkFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
    
class GalleryModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Gallerys.
    Can only be done by superuser.
    '''
    
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = GalleryFilter
    search_field = ['link_id', 'caption']
    pagination_class = Pagination
    
    
class FAQUserModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting FAQUsers.
    Can only be done by superuser.
    '''
    
    queryset = FAQUser.objects.all()
    serializer_class = FAQUserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FAQUserFilter
    search_field = ['link_id', 'username', 'biography']
    pagination_class = Pagination
    