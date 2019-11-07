from django.db import models
from users.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=128, blank=False)
    last_message = models.CharField(max_length=4096, blank=False)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="chat id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="users id")
    content = models.CharField(max_length=4096, blank=False)
    added_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name="Time and Date of sending",
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-added_at']


class Attachment(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name="chat id",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="users id",
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name="message id",
    )
    type = models.CharField(
        max_length=10,
        blank=False,
    )
    url = models.URLField(
        max_length=200,
        blank=False,
    )

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'