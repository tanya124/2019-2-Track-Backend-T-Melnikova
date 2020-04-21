from .views import start_page, profile, search_user
from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
        path('', start_page, name='start_page'),
        path('profile/', profile, name='profile'),
        path('user/<str:nick>/', search_user, name='search_user'),
        path('api/', include(router.urls))
    ]
