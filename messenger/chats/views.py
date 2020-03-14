from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from chats.models import Chat, Message
from users.models import Member, User
from chats.forms import ChatForm, MessageForm, MemberForm, AttachmentForm
from application.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import boto3


@login_required
def chat_list(request):
    if request.method == 'GET':
        user = request.user
        chats = Chat.objects.values('id', 'topic', 'is_group_chat', 'last_message').filter(member__user_id=user.id)
        return JsonResponse({'chats': list(chats)})
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def contacts_list(request):
    if request.method == 'GET':
        users = User.objects.values('id', 'nick', 'avatar')
        return JsonResponse({'users' : list(users)})
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def chat_page(request):
    if request.method == 'GET':
        chat_id = request.GET['chat_id']
        user = request.user
        messages_from_chat = Message.objects.values('id', 'content', 'added_at', 'user__username').filter(chat=chat_id).order_by('added_at')
        return JsonResponse({'messages': list(messages_from_chat)})
    else:
        return HttpResponseNotAllowed(['GET'])

#добавить обработку ошибок fields = ['is_group_chat', 'topic', 'last_message']
@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        companion_name = request.POST['companion_name']

        if form.is_valid():
            is_group_chat = request.POST.get('is_group_chat')
            topic = request.POST.get('topic', 'new chat')
            last_message = request.POST.get('last_message', 'empty')
            cur_user = request.user
            #cur_user = User.objects.get(id=6)
            companion = User.objects.get(username=companion_name)

            new_chat = Chat.objects.create(is_group_chat=is_group_chat, topic=topic, last_message=last_message)
            new_member = Member.objects.create(user=cur_user, chat=new_chat, new_messages=0)
            new_member_companion = Member.objects.create(user=companion, chat=new_chat, new_messages=0)
            return JsonResponse({'chat name':new_chat.topic}, status=201)
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def add_member_to_chat(request):
    if request.method == 'POST':
        chat_id = request.POST['chat_id']
        added_username = request.POST['username']
        chat = Chat.objects.get(id=chat_id)
        user = User.objects.get(username=added_username)
        new_member = Member.objects.create(user=user, chat=chat, new_messages=0)
        return JsonResponse({'member': new_member.id}, status=200)
    else:
        return HttpResponseNotAllowed(['POST'])

#fields = ['chat', 'content']
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        chat_id = request.POST.get('chat')
        user_id = request.user.id

        if form.is_valid():
            content = request.POST.get('content')
            chat = Chat.objects.get(id=chat_id)
            user = User.objects.get(id=user_id)

            new_message = Message.objects.create(chat=chat, user=user, content=content)
            return JsonResponse({'msg' : new_message.content, 'user': new_message.user_id, 'chat':new_message.chat_id})
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def get_list_message(request, chat_id):
    if request.method == 'GET':
        messages = Message.objects.values('chat', 'user', 'content', 'added_at')
        messages_from_chat = messages.filter(chat = chat_id)
        return JsonResponse({'messages': list(messages_from_chat)})

    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def read_message(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        user_id = request.user.id
        chat_id = request.POST.get('chat')
        if form.is_valid():
            member = Member.objects.all().filter(user=user_id).filter(chat=chat_id)
            messages_from_chat = Message.objects.all().filter(chat=chat_id).order_by('added_at')
            member.last_read_message = messages_from_chat.last()
            return JsonResponse({'last read message': member.last_read_message.id})
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])


def upload_file(filename):
    file_descriptor = open(filename, mode='rb')
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    key = 'attachment/' + file_descriptor.name.split('/')[-1]
    return s3_client.put_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=key, Body=file_descriptor.read())

@login_required
def attach_file(request):
    if request.method == 'POST':
        file_path = request.POST.get('path')
        url = upload_file(file_path)
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save()
            attachment.url = url
            return JsonResponse({
                'attachment': {
                    'id': attachment.id,
                    'chat_id': attachment.chat.id,
                    'user_id': attachment.user.id,
                    'message': attachment.message.content,
                    'type': attachment.type,
                    'url': attachment.url.url,
                }
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])