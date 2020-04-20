import random
import json
from django.test import TestCase, Client
from users.models import User, Member
from chats.models import Chat
from django.urls import reverse
from chats.factories import ChatsFactory, MessageFactory, MemberFactory
from users.factories import UserFactory
from mock import patch


class ChatsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user_1", password="test", nick="test_user_1_nick")
        self.client.force_login(self.user)

        self.users = UserFactory.build_batch(5, nick='common_nick')
        for user in self.users:
            user.save()

        self.chats = ChatsFactory.build_batch(5)

        for current_chat in self.chats:
            current_chat.save()
            Member.objects.create(user=self.user, chat=current_chat)

        self.messages_from_chat_0 = MessageFactory.build_batch(5, chat=self.chats[0], user=self.user)
        for msg in self.messages_from_chat_0:
            msg.save()


    def test_chat_list(self):
        response = self.client.get(reverse('chat_list', kwargs={}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(len(content['chats']), len(self.chats))


    def test_contacts_list(self):
        response = self.client.get(reverse('contacts_list', kwargs={}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(len(content['users']), len(self.users) + 1)

    def test_chat_page(self):
        chat = self.chats[0]
        response = self.client.get(reverse('chat_page'), {'chat_id': chat.id})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), 5)

    def test_create_chat(self):
        response = self.client.post(reverse('create_chat'), {'companion_name': self.users[0].username, 'topic': 'new chat', 'last_message': 'NULL', 'is_group_chat': False})
        self.assertTrue(response.status_code == 201)
        content = json.loads(response.content)
        self.assertEqual(content['chat_name'], 'new chat')

    def test_add_member_to_chat(self):
        response = self.client.post(reverse('add_member_to_chat'), {'chat_id': self.chats[0].id, 'username': self.users[1].username})
        self.assertTrue(response.status_code == 200)
        #content = json.loads(response.content)

    def test_send_message(self):
        response = self.client.post(reverse('send_message'), {'chat': self.chats[0].id, 'user': self.user.id, 'content': 'msg'})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'msg')
        self.assertEqual(content['user'], self.user.id)
        self.assertEqual(content['chat'], self.chats[0].id)

    def test_get_list_message(self):
        response = self.client.get(reverse('get_list_message', kwargs={'chat_id' : self.chats[0].id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), len(self.messages_from_chat_0))

    def test_read_message(self):
        response = self.client.post(reverse('read_message'), {'chat': self.chats[0].id, 'user': self.user.id})
        self.assertTrue(response.status_code == 200)
        #content = json.loads(response.content)

    @patch('chats.views.upload_file')
    def test_attach_file(self, upload_file_mock):
        upload_file_mock.return_value = 'attachment/'
        response = self.client.post(reverse('attach_file'), {'chat': self.chats[0].id, 'user': self.user.id, 'message': self.messages_from_chat_0[0].id, 'path': '/home/tanya/track/2019-2-Track-Backend-T-Melnikova/test/cat2.jpg'})
        self.assertTrue(response.status_code == 200)
        self.assertEqual(upload_file_mock.call_count, 1)


    def tearDown(self):
        a = ['ヽ(・∀・)ﾉ', 'ヽ(*・ω・)ﾉ', '(◕‿◕)']
        print('Chats unittests: success {0}'.format(a[random.randint(0, 2)]))


