from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions, generics


from knox.models import AuthToken
from .serializers import (CreateUserSerializer,
                          UserSerializer, LoginUserSerializer)
from .models import User


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
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


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
