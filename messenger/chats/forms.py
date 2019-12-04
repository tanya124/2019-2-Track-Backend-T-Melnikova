from django import forms
from chats.models import Chat, Message
from users.models import Member, User


class ChatForm(forms.Form):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'content']

    def clean(self):
        chat = self.cleaned_data.get('chat')
        user = self.cleaned_data.get('user')
        if chat is None:
            self._errors['chat'] = self.error_class(["Chat does not exist"])
        if user is None:
            self._errors['user'] = self.error_class(["User does not exist"])
        return self.cleaned_data


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'chat']

    def clean(self):
        member = self.cleaned_data.get('user')
        chat = self.cleaned_data.get('chat')
        if member is None:
            self._errors['user'] = self.error_class(["Member does not exist"])
        if chat is None:
            self._errors['chat'] = self.error_class(["Chat does not exist"])
        return  self.cleaned_data