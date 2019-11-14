from django import forms
from chats.models import Chat, Message
from users.models import Member


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'content']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'chat']