from django.urls import path
from chats.views import chat_list, contacts_list, chat_page, create_chat, send_message, get_list_message
from chats.views import read_message, attach_file

urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('contacts_list/', contacts_list, name='contacts_list'),
        path('chat_page/', chat_page, name='chat_page'),
        path('create_chat/', create_chat, name='create_chat'),
        path('send_message/', send_message, name='send_message'),
        path('get_messages/<int:chat_id>/', get_list_message, name='get_list_message'),
        path('read_message/', read_message, name='read_message'),
        path('attach/', attach_file, name='attach_file'),
        ]