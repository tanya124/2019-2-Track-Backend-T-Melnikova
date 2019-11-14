from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Message
from users.models import Member, User
from chats.forms import ChatForm, MessageForm, MemberForm


def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.values('id', 'topic', 'is_group_chat', 'last_message')
        return JsonResponse({'chats': list(chats)})
    else:
        return HttpResponseNotAllowed(['GET'])


def contacts_list(request):
    if request.method == 'GET':
        users = User.objects.values('id', 'nick', 'avatar')
        return JsonResponse({'users' : list(users)})
    else:
        return HttpResponseNotAllowed(['GET'])


def chat_page(request):
    if request.method == 'GET':
        id = request.GET.get("id", 1)
        return JsonResponse({'chat' : id})
    else:
        return HttpResponseNotAllowed(['GET'])


def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)

        if form.is_valid():
            user_id = request.POST.get('user_id', False)

            if user_id is False:
                return HttpResponseBadRequest

            is_group_chat = request.POST.get('is_group_chat', False)
            topic = request.POST.get('topic', 'new chat')
            cur_user = User.objects.get(id=user_id)

            new_chat = Chat.objects.create(is_group_chat=is_group_chat, topic=topic)
            new_member = Member.objects.create(user=cur_user, chat=new_chat, new_messages=0)
            return JsonResponse({'new_chat_id': new_chat.id, 'chat name':new_chat.topic, 'member_id': new_member.id}, status=201)
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            chat_id = request.POST.get('chat', False)
            user_id = request.POST.get('user', False)
            content = request.POST.get('content', False)

            if chat_id is False or user_id is False or content is False:
                return HttpResponseBadRequest

            chat = Chat.objects.get(id=chat_id)
            user = User.objects.get(id=user_id)

            new_message = Message.objects.create(chat=chat, user=user, content=content)
            return JsonResponse({'msg' : new_message.content, 'user': new_message.user_id, 'chat':new_message.chat_id})
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])


def get_list_message(request, chat_id):
    if request.method == 'GET':
        messages = Message.objects.values('chat', 'user', 'content', 'added_at')
        messages_from_chat = messages.filter(chat = chat_id)
        return JsonResponse({'messages': list(messages_from_chat)})

    else:
        return HttpResponseNotAllowed(['GET'])


def read_message(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member_id = request.POST.get('member_id', False)
            if member_id is False:
                return HttpResponseBadRequest
            member = Member.objects.get(id=member_id)
            chat_id = member.chat.id
            messages_from_chat = Message.objects.all().filter(chat_id=chat_id).order_by('added_at')
            member.last_read_message = messages_from_chat.last()
            return JsonResponse({'last read message': member.last_read_message.id})
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

# HW7
# 1)send_message +
# 2)get_list_messages_of_chat +
# 3)read_message +
# 4)валидировать с помощью форм
# 5)переписать заглушки