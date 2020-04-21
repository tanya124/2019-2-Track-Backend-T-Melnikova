from rest_framework import serializers
from .models import Chat, Message, Attachment


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'topic', 'is_group_chat', 'last_message')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'added_at', 'user')


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('id', 'chat', 'user', 'message', 'type', 'url')