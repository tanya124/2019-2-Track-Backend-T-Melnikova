from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    nick = forms.CharField(max_length=128, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'nick', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        user = self.cleaned_data.get('username')
        if user is None:
            self._errors['user'] = self.error_class(["User does not exist or password is wrong"])

        return self.cleaned_data

