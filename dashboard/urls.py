from django.urls import path, include
from .views import (
    MainLinkView,
    DashboardView,
    MainLinkDelete
)

app_name = 'dashboard'


urlpatterns = [
    path('Link/<str:link_name>/', MainLinkView.as_view(), name='main_link'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/', MainLinkDelete.as_view(), name='main_link_delete'),
    
    # API
    path('dashboard/api/v1/', include('dashboard.api.v1.urls'))
]