from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Message
from users.models import Member, User


def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.values('id', 'topic', 'is_group_chat', 'last_message')
        return JsonResponse({'chats': list(chats)})
    else:
        return HttpResponseNotAllowed(['GET'])


def contacts_list(request):
    if request.method == 'GET':
        return JsonResponse({'contacts' : 'list'})
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
        user_id = request.POST.get('user_id', 0)
        is_group_chat = request.POST.get('is_group_chat', False)
        topic = request.POST.get('topic', 'new chat')
        content = request.POST.get('content', 'New message')
        cur_user = User.objects.get(id=user_id)

        new_chat = Chat.objects.create(is_group_chat=is_group_chat, topic=topic)
        new_message = Message.objects.create(chat=new_chat, user=cur_user, content=content)
        new_member = Member.objects.create(user=cur_user, chat=new_chat, new_messages=0, last_read_message=new_message)
        return JsonResponse({'new_chat_id': new_chat.id, 'chat name':new_chat.topic, 'member_id': new_member.id}, status=201)
    else:
        return HttpResponseNotAllowed(['POST'])