from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from .models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import UserSerializer
from django.views.decorators.cache import cache_page



@login_required
def start_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')
    else:
        return HttpResponseNotAllowed(['GET'])

@cache_page(60 * 15)
@login_required
def profile(request):
    if request.method == 'GET':
        return JsonResponse({
            'profile' : {'user_id': request.user.id, 'username': request.user.username}
        })
    else:
        return HttpResponseNotAllowed(['GET'])

@cache_page(60 * 15)
@login_required
def search_user(request, nick):
    if request.method == 'GET':
        user = User.objects.values('id', 'username', 'nick')
        user = user.filter(nick__icontains = nick)
        return JsonResponse({'users': list(user)})
    else:
        return HttpResponseNotAllowed(['GET'])


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #http://127.0.0.1:8000/users/api/users/profile/
    @action(methods=['get'], detail=False)
    def profile(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user, many=False)
        return Response({"user": serializer.data})


    #http://127.0.0.1:8000/users/api/users/search_user/?nick=user_1
    @action(methods=['get'], detail=False)
    def search_user(self, request):
        nick = request.GET['nick']
        user = User.objects.filter(nick__icontains=nick)
        serializer = UserSerializer(user, many=True)
        return Response({"user": serializer.data})
