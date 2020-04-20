import json
from django.test import TestCase, Client
from users.models import User
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BlogTest(TestCase):
    def setUp(self):
        self.auth_client = Client()
        self.user1 = User.objects.create(username="test_user_1", password="test", nick="test1")
        self.user1.save()
        self.auth_client.force_login(self.user1)

        self.no_auth_client = Client()
        self.user2 = User.objects.create(username="test_user_2", password="test", nick="test2")
        self.user2.save()
        self.new_client = Client()

    def test_home(self):
        response = self.auth_client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)

        response = self.no_auth_client.get(reverse('home'))
        self.assertFalse(response.status_code == 200)

    def test_register(self):
        response = self.new_client.post(reverse('register'), {
            'username': 'new_user',
            'nick': 'new_user_nick',
            'first_name': 'name',
            'second_name': 'surname',
            'email': 'qwerty@test.ru',
            'password1': 'vbvbvb***',
            'password2': 'vbvbvb***'
        })
        self.assertTrue(response.status_code == 200)

    # def test_login(self):
    #     response = self.no_auth_client.post(reverse('login'), {'username': self.user2.username, 'password': 'wrong password'})
    #     self.assertFalse(response.status_code == 200)
    #     content = json.loads(response.content)
    #     self.assertEqual(content['errors'], 'invalid login')

        # response = self.no_auth_client.post(reverse('login'), {
        #         'username': self.user2.username,
        #         'password': self.user2.password
        #     })
        # content = json.loads(response.content)
        # self.assertTrue(response.status_code == 200)


    # def test_logout(self):
    #     response = self.auth_client.post(reverse('logout'))
    #     self.assertTrue(response.status_code == 200)


class SileniumTest(TestCase):
    def setUp(self):
        self.webdriver = webdriver.Chrome('/home/tanya/chromedriver')
        self.webdriver.implicitly_wait(10)
        self.webdriver.get('http://localhost:8000/login/')

    def test_login(self):
        login_input = self.webdriver.find_element_by_name('username')
        password_input = self.webdriver.find_element_by_name('password')
        assert login_input is not None
        assert password_input is not None

        login_input.send_keys('test_user')
        password_input.send_keys('passwprd')

        submit_btn = self.webdriver.find_element_by_xpath('//*[@type="submit"]')
        assert submit_btn is not None
        submit_btn.click()


    def tearDown(self):
        self.webdriver.close()
        print('Seleneum test success')

