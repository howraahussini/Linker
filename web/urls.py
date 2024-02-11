from django.urls import path, include

from .views import (
    IndexView,
    ContactView
)

app_name = 'web'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),

    
    # API
    path('web/api/v1/', include('web.api.v1.urls'))
]