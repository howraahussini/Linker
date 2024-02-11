from django.urls import path, include
from .views import (
    
    SocialView,

    # Email
    EmailView,
    EmailEditView,
    EmailDeleteView,

    # Phon
    PhoneView,
    PhoneEditView,
    PhoneDeleteView,

    # Instagram
    InstagramView,
    InstagramEditView,
    InstagramDeleteView,

    # Telegram
    TelegramView,
    TelegramEditView,
    TelegramDeleteView,

    # Youtube
    YoutubeView,
    YoutubeEditView,
    YoutubeDeleteView,

    # Whatsapp
    WhatsappView,
    WhatsappEditView,
    WhatsappDeleteView,

    # X
    XView,
    XEditView,
    XDeleteView,

    # Facebook
    FacebookView,
    FacebookEditView,
    FacebookDeleteView,

    # Linkedin
    LinkedinView,
    LinkedinEditView,
    LinkedinDeleteView,

    # Snapchat
    SnapchatView,
    SnapchatEditView,
    SnapchatDeleteView,

    # Tiktok
    TiktokView,
    TiktokEditView,
    TiktokDeleteView,
)


app_name = 'social'


urlpatterns = [

    path('<str:link_name>/', SocialView.as_view(), name='social'),

    # Email
    path('<str:link_name>/email/form/', EmailView.as_view(), name='email'),
    path('<str:link_name>/email/edit/<int:pk>/', EmailEditView.as_view(), name='email_edit'),
    path('<str:link_name>/email/delete/<int:pk>/', EmailDeleteView.as_view(), name='email_delete'),

    # Phone
    path('<str:link_name>/phone/form/', PhoneView.as_view(), name='phone'),
    path('<str:link_name>/phone/edit/<int:pk>/', PhoneEditView.as_view(), name='phone_edit'),
    path('<str:link_name>/phone/delete/<int:pk>/', PhoneDeleteView.as_view(), name='phone_delete'),

    # Instagram
    path('<str:link_name>/instagram/form/', InstagramView.as_view(), name='instagram'),
    path('<str:link_name>/instagram/edit/<int:pk>/', InstagramEditView.as_view(), name='instagram_edit'),
    path('<str:link_name>/instagram/delete/<int:pk>/', InstagramDeleteView.as_view(), name='instagram_delete'),

    # Telegram
    path('<str:link_name>/telegram/form/', TelegramView.as_view(), name='telegram'),
    path('<str:link_name>/telegram/edit/<int:pk>/', TelegramEditView.as_view(), name='telegram_edit'),
    path('<str:link_name>/telegram/delete/<int:pk>/', TelegramDeleteView.as_view(), name='telegram_delete'),

    # Youtube
    path('<str:link_name>/youtube/form/', YoutubeView.as_view(), name='youtube'),
    path('<str:link_name>/youtube/edit/<int:pk>/', YoutubeEditView.as_view(), name='youtube_edit'),
    path('<str:link_name>/youtube/delete/<int:pk>/', YoutubeDeleteView.as_view(), name='youtube_delete'),

    # Whatsapp
    path('<str:link_name>/whatsapp/form/', WhatsappView.as_view(), name='whatsapp'),
    path('<str:link_name>/whatsapp/edit/<int:pk>/', WhatsappEditView.as_view(), name='whatsapp_edit'),
    path('<str:link_name>/whatsapp/delete/<int:pk>/', WhatsappDeleteView.as_view(), name='whatsapp_delete'),

    # X
    path('<str:link_name>/x/form/', XView.as_view(), name='x'),
    path('<str:link_name>/x/edit/<int:pk>/', XEditView.as_view(), name='x_edit'),
    path('<str:link_name>/x/delete/<int:pk>/', XDeleteView.as_view(), name='x_delete'),

    # Facebook
    path('<str:link_name>/facebook/form/', FacebookView.as_view(), name='facebook'),
    path('<str:link_name>/facebook/edit/<int:pk>/', FacebookEditView.as_view(), name='facebook_edit'),
    path('<str:link_name>/facebook/delete/<int:pk>/', FacebookDeleteView.as_view(), name='facebook_delete'),

    # Linkedin
    path('<str:link_name>/linkedin/form/', LinkedinView.as_view(), name='linkedin'),
    path('<str:link_name>/linkedin/edit/<int:pk>/', LinkedinEditView.as_view(), name='linkedin_edit'),
    path('<str:link_name>/linkedin/delete/<int:pk>/', LinkedinDeleteView.as_view(), name='linkedin_delete'),

    # Snapchat
    path('<str:link_name>/snapchat/form/', SnapchatView.as_view(), name='snapchat'),
    path('<str:link_name>/snapchat/edit/<int:pk>/', SnapchatEditView.as_view(), name='snapchat_edit'),
    path('<str:link_name>/snapchat/delete/<int:pk>/', SnapchatDeleteView.as_view(), name='snapchat_delete'),

    # Tiktok
    path('<str:link_name>/tiktok/form/', TiktokView.as_view(), name='tiktok'),
    path('<str:link_name>/tiktok/edit/<int:pk>/', TiktokEditView.as_view(), name='tiktok_edit'),
    path('<str:link_name>/tiktok/delete/<int:pk>/', TiktokDeleteView.as_view(), name='tiktok_delete'),
    
    
    # API
    path('api/v1/', include('social_media.api.v1.urls'))
]