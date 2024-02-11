from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('main_link', views.MainLinkModelViewSet, basename='main_link')
router.register('main_link/template', views.MainLinkTemplateModelViewSet, basename='main_link_template')

urlpatterns = router.urls