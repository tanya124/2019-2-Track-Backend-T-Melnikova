import json
from django.test import TestCase, Client
from users.models import User
from django.urls import reverse

class UsersTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user_1")
        self.client.force_login(self.user)

    def test_search_user(self):
        response = self.client.get(reverse('profile', kwargs={}))

