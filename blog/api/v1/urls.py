from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api_v1'

router = DefaultRouter()

router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
router.register('comments', views.CommentModelViewSet, basename='comments')


urlpatterns = router.urls