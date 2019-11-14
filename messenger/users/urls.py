from users.views import start_page, profile, search_user
from django.urls import path

urlpatterns = [
        path('', start_page, name='start_page'),
        path('profile/', profile, name='profile'),
        path('user/<int:user_id>/', search_user, name='search_user'),
    ]