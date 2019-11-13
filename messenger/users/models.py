from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    nick = models.CharField(max_length=128, blank=True, default='')
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="users id")
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE, verbose_name="chat id")
    new_messages = models.BooleanField(default=True)
    last_read_message = models.ForeignKey('chats.Message', on_delete=models.PROTECT, verbose_name="last read message")

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чата'