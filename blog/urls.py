from django.urls import path, include
from .views import (
    PostView,
    PostSingleView,
    CategorySearch
)

app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='blog'),
    path('<int:pk>/', PostSingleView.as_view(), name='post_single'),
    path("category/<str:cat>/", CategorySearch.as_view(), name="category"),

    # API
    path('api/v1/', include('blog.api.v1.urls')),
]