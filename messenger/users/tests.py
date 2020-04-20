import json
from django.test import TestCase, Client
from users.models import User
from django.urls import reverse
from users.factories import UserFactory
import random


class UsersTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user_1", password="test", nick="test_user_1_nick")
        self.client.force_login(self.user)
        self.users = UserFactory.build_batch(5, nick='common_nick')

    def test_profile(self):
        response = self.client.get(reverse('profile', kwargs={}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['profile']['username'], 'test_user_1')

    def test_search_user(self):
        response = self.client.get(reverse('search_user', kwargs={'nick': 'common_nick'}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        for person in content['users']:
            self.assertEqual(person['nick'], 'common_nick')

    def test_start_page(self):
        response = self.client.get(reverse('start_page', kwargs={}))
        self.assertTrue(response.status_code == 200)

    def tearDown(self):
        a = ['ヽ(・∀・)ﾉ', 'ヽ(*・ω・)ﾉ', '(◕‿◕)']
        print('Users unittests: success {0}'.format(a[random.randint(0, 2)]))
