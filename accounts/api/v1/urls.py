from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api_v1'

router = DefaultRouter()
router.register('', views.AccountModelViewSet, basename='accounts_api')

urlpatterns = router.urls