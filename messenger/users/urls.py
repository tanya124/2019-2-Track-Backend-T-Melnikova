from .views import start_page, profile, search_user
from django.urls import path, include
from .views import UserViewSet,  RegistrationAPI, LoginAPI, UserAPI
from rest_framework import routers
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
        path('', start_page, name='start_page'),
        path('profile/', profile, name='profile'),
        path('user/<str:nick>/', search_user, name='search_user'),
        path('api/', include(router.urls)),
        path('auth/register/', RegistrationAPI.as_view()),
        path('auth/login/', LoginAPI.as_view()),
        path('auth/user/', UserAPI.as_view()),
        path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    ]
