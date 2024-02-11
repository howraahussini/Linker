from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from accounts.api.v1.pagination import Pagination

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

from .serializers import (
    EmailSerializer,
    PhoneSerializer,
    InstagramSerializer,
    TelegramSerializer,
    YoutubeSerializer,
    WhatsappSerializer,
    XSerializer,
    FacebookSerializer,
    LinkedinSerializer,
    SnapchatSerializer,
    TiktokSerializer
)

from .filters import (
    EmailFilter,
    PhoneFilter,
    InstagramFilter,
    TelegramFilter,
    YoutubeFilter,
    WhatsappFilter,
    XFilter,
    FacebookFilter,
    LinkedinFilter,
    SnapchatFilter,
    TiktokFilter
)


class EmailModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Emails.
    Can only be done by superuser.
    '''
    
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmailFilter
    search_field = ['link_id', 'title', 'email']
    pagination_class = Pagination
    
    
class PhoneModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Phones.
    Can only be done by superuser.
    '''
    
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PhoneFilter
    search_field = ['link_id', 'title', 'number']
    pagination_class = Pagination
    
    
class InstagramModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Instagrams.
    Can only be done by superuser.
    '''
    
    queryset = Instagram.objects.all()
    serializer_class = InstagramSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = InstagramFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
class TelegramModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Telegrams.
    Can only be done by superuser.
    '''
    
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TelegramFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
class YoutubeModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Youtubes.
    Can only be done by superuser.
    '''
    
    queryset = Youtube.objects.all()
    serializer_class = YoutubeSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = YoutubeFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
class WhatsappModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Whatsapps.
    Can only be done by superuser.
    '''
    
    queryset = Whatsapp.objects.all()
    serializer_class = WhatsappSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WhatsappFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
class XModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Xs.
    Can only be done by superuser.
    '''
    
    queryset = X.objects.all()
    serializer_class = XSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = XFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
class FacebookModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Facebooks.
    Can only be done by superuser.
    '''
    
    queryset = Facebook.objects.all()
    serializer_class = FacebookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FacebookFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
    
class LinkedinModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Linkedins.
    Can only be done by superuser.
    '''
    
    queryset = Linkedin.objects.all()
    serializer_class = LinkedinSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LinkedinFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
    
class SnapchatModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Snapchats.
    Can only be done by superuser.
    '''
    
    queryset = Snapchat.objects.all()
    serializer_class = SnapchatSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SnapchatFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
    
    
class TiktokModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Tiktoks.
    Can only be done by superuser.
    '''
    
    queryset = Tiktok.objects.all()
    serializer_class = TiktokSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TiktokFilter
    search_field = ['link_id', 'title', 'link']
    pagination_class = Pagination
