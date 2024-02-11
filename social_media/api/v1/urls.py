from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()


router.register('email', views.EmailModelViewSet, basename='email')
router.register('phone', views.PhoneModelViewSet, basename='phone')
router.register('instagram', views.InstagramModelViewSet, basename='instagram')
router.register('telegram', views.TelegramModelViewSet, basename='telegram')
router.register('youtube', views.YoutubeModelViewSet, basename='youtube')
router.register('whatsapp', views.WhatsappModelViewSet, basename='whatsapp')
router.register('x', views.XModelViewSet, basename='x')
router.register('facebook', views.FacebookModelViewSet, basename='facebook')
router.register('linkedin', views.LinkedinModelViewSet, basename='linkedin')
router.register('snapchat', views.SnapchatModelViewSet, basename='snapchat')
router.register('tiktok', views.TiktokModelViewSet, basename='tiktok')


urlpatterns = router.urls