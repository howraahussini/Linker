from rest_framework.routers import DefaultRouter

from . import views 

router = DefaultRouter()

router.register('contact', views.ContactModelViewSet, basename='contact')
router.register('faq', views.FAQModelViewSet, basename='faq')

urlpatterns = router.urls