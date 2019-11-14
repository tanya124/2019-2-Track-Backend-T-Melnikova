from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from users.models import User


def start_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')
    else:
        return HttpResponseNotAllowed(['GET'])


def profile(request):
    if request.method == 'GET':
        return JsonResponse({'my' : 'profile'})
    else:
        return HttpResponseNotAllowed(['GET'])


def search_user(request, user_id):
    if request.method == 'GET':
        user = User.objects.values('id', 'nick', 'avatar')
        user = get_object_or_404(user, id = user_id)
        return JsonResponse({'user': dict(user)})
    else:
        return HttpResponseNotAllowed(['GET'])

