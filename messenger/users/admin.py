from django.contrib import admin
from users.models import User, Member


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','nick')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'user', 'new_messages', 'last_read_message')


admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)

