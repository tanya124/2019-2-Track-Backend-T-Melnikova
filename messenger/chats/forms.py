from django import forms
from chats.models import Chat, Message, Attachment
from users.models import Member, User

class ChatForm(forms.Form):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic', 'last_message']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        #fields = ['chat', 'user', 'content']
        fields = ['chat', 'content']

    def clean(self):
        chat = self.cleaned_data.get('chat')
        #user = self.cleaned_data.get('user')
        if chat is None:
            self._errors['chat'] = self.error_class(["Chat does not exist"])
        #if user is None:
        #    self._errors['user'] = self.error_class(["User does not exist"])
        return self.cleaned_data


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['chat', 'user']

    def clean(self):
        chat = self.cleaned_data.get('chat')

        if chat is None:
            self._errors['chat'] = self.error_class(["Chat does not exist"])
        return  self.cleaned_data


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['chat', 'user', 'message']
        #fields = ['chat', 'message']