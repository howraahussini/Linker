from django.urls import path, include
from .views import (
    SignUpView,
    LoginView,
    AccountView,
)


app_name = 'accounts'

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('<str:link_name>/accounts/<int:pk>', AccountView.as_view(), name='account'),
    
    
    # API
    path('accounts/api/v1/', include('accounts.api.v1.urls')),
]