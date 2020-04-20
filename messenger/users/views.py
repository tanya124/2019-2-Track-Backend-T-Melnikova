from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from users.models import User

@login_required
def start_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def profile(request):
    if request.method == 'GET':
        return JsonResponse({
            'profile' : {'user_id': request.user.id, 'username': request.user.username}
        })
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def search_user(request, nick):
    if request.method == 'GET':
        user = User.objects.values('id', 'username', 'nick')
        user = user.filter(nick__icontains = nick)
        return JsonResponse({'users': list(user)})
    else:
        return HttpResponseNotAllowed(['GET'])

