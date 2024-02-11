from django.urls import path, include
from .views import (
    ModulesPageView,
    ProfileEditView,
    MainLinkTemplateView,

    # Text
    TextView,
    TextEditView,
    TextDeleteView,

    # Link
    LinkView,
    LinkEditView,
    LinkDeleteView,
    
    # Gallery
    GalleryView,
    GalleryEditView,
    GalleryDeleteView,   

    # FaqUser
    FAQUserView,
    FAQUserEditView,
    FAQUserDeleteView,

)


app_name = 'panel'



urlpatterns = [

  path('<str:link_name>/edit/', ModulesPageView.as_view(), name='modules_page'),

  # Profile
  path('<str:link_name>/profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile'),
  
  # Main Link Template
  path('<str:link_name>/template/<int:pk>', MainLinkTemplateView.as_view(), name='main_link_template'),

  # Text
  path('<str:link_name>/text/form/', TextView.as_view(), name='text'),
  path('<str:link_name>/text/edit/<int:pk>/', TextEditView.as_view(), name='text_edit'),
  path('<str:link_name>/text/delete/<int:pk>/', TextDeleteView.as_view(), name='text_delete'),
  
  # Link
  path('<str:link_name>/link/form/', LinkView.as_view(), name='link'),
  path('<str:link_name>/link/edit/<int:pk>/', LinkEditView.as_view(), name='link_edit'),
  path('<str:link_name>/link/delete/<int:pk>/', LinkDeleteView.as_view(), name='link_delete'),

  # Gallery
  path('<str:link_name>/gallery/form/', GalleryView.as_view(), name='gallery'),  
  path('<str:link_name>/gallery/edit/<int:pk>/', GalleryEditView.as_view(), name='gallery_edit'),
  path('<str:link_name>/gallery/delete/<int:pk>/', GalleryDeleteView.as_view(), name='gallery_delete'),

  # FaqUser
  path('<str:link_name>/faq_users/form/', FAQUserView.as_view(), name='faq_user'),
  path('<str:link_name>/faq_user/edit/<int:pk>/', FAQUserEditView.as_view(), name='faq_user_edit'),
  path('<str:link_name>/faq_user/delete/<int:pk>/', FAQUserDeleteView.as_view(), name='faq_user_delete'),
  
  # API 
  path('api/v1/', include('panel.api.v1.urls'))
  
]