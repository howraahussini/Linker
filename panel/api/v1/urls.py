from rest_framework.routers import DefaultRouter 
from . import views 


router = DefaultRouter()

router.register('profile', views.ProfileModelViewSet, basename='profile')
router.register('text', views.TextModelViewSet, basename='text')
router.register('link', views.LinkModelViewSet, basename='link')
router.register('gallery', views.GalleryModelViewSet, basename='gallery')
router.register('faq_user', views.FAQUserModelViewSet, basename='faq_user')

urlpatterns = router.urls