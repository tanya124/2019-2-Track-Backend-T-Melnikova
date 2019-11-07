from users.views import start_page
from users.views import profile
from django.urls import path

urlpatterns = [
        path('', start_page, name='start_page'),
        path('profile/', profile, name='profile'),
    ]