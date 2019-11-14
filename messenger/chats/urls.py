from django.urls import path
from chats.views import chat_list, contacts_list, chat_page, create_chat


urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('contacts_list/', contacts_list, name='contacts_list'),
        path('chat_page/', chat_page, name='chat_page'),
        path('create_chat/', create_chat, name='create_chat'),
        ]