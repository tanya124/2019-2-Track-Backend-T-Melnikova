from django.contrib import admin
from chats.models import Chat, Message, Attachment


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','is_group_chat','topic', 'last_message')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'user', 'content', 'added_at')


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'user', 'message', 'type', 'url', )


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Attachment, AttachmentAdmin)
