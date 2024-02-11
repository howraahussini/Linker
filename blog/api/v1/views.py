from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from accounts.api.v1.pagination import Pagination

from ...models import Category, Comment, Post
from .filters import PostFilter, CommentFilter
from .serializers import (
    PostSerializer,
    CategorySerializer,
    CommentSerializer    
)

class PostModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Posts.
    Can only be done by superuser.
    '''
    
    queryset = Post.objects.filter(status = True)
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_field = ['author', 'title', 'categories']
    pagination_class = Pagination
    

class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    class CategoryModelViewSet is for category api model.
    """

    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    '''
    This class is for listing, creating, updating and deleting Comments
    Can only be done by superuser.
    '''
    
    queryset = Comment.objects.filter(approved = True)
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]    
    filterset_class = CommentFilter
    search_field = ['post', 'name', 'email']
    pagination_class = Pagination
    