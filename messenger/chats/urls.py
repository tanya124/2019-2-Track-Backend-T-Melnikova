from django.urls import path
from chats.views import chat_list
from chats.views import contacts_list
from chats.views import chat_page

urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('contacts_list/', contacts_list, name='contacts_list'),
        path('chat_page/', chat_page, name='chat_page')
        ]