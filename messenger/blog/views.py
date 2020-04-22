from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from chats.models import Chat
from django.contrib.auth import authenticate, login, logout
from . import forms


@login_required
def home(request):
    return render(request, 'home.html')


#fields = ('username', 'nick', 'first_name', 'last_name', 'email', 'password1', 'password2',)
def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'username': request.POST['username']})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

# def my_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return JsonResponse({'result' : 'ok'}, status=200)
#             else:
#                 return JsonResponse({'errors': 'disabled account'}, status=400)
#         else:
#             return JsonResponse({'errors': 'invalid login'}, status=400)
#     else:
#         return HttpResponseNotAllowed(['POST'])

# @login_required
# def my_logout(request):
#     if request.method == 'POST':
#         logout(request)
#         return JsonResponse({'result' : 'ok'})
#     else:
#         return HttpResponseNotAllowed(['POST'])


# def login(request):
#     if request.method == 'GET':
#         form = UserForm(request.GET)
#         username = request.GET.get("username")
#         password = request.GET.get("password")
#         if form.is_valid():
#             user = User.objects.get(username=username)
#             if check_password(password, user.password):
#                 # авторизация
#                 chats = Chat.objects.values('id', 'is_group_chat', 'topic', 'last_message').filter(member__user_id=user.id)
#                 return JsonResponse({'chats' : list(chats)})
#             else:
#                 return JsonResponse({'errors' : 'password is wrong'})
#         else:
#             return JsonResponse({'errors': form.errors})
#     else:
#         return HttpResponseNotAllowed(['GET'])

