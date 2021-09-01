from django.http import request
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
from users.views import UserView, GetUserView
from users.models import User
import jwt, datetime
from yieldPrediction.settings import SECRET_KEY

factory = APIRequestFactory()


class UserTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.userData = {'email': 'test@test.com', 'password': 'testpassword'}
        #self.testUser = User.objects.create(email = 'test@test.com', password = 'testpassword')
        #self.testUser.is_active = True
        #self.testUser.save()

    def test_post_content(self):
        request = self.factory.post('/user/', data = self.userData)
        response = UserView.as_view()(request)

        self.assertEquals(response.data['user']['email'], 'test@test.com')
        self.assertEquals(response.status_code, 202)

    def test_get_content(self):
        postRequest = self.factory.post('/user/', data = self.userData)
        postResponse = UserView.as_view()(postRequest)
        ID = postResponse.data["user"]["id"]

        getRequest = self.factory.get(f'/user/1')
        getResponse = GetUserView.as_view()(getRequest, idUser=ID, authed=True)

        self.assertEquals(getResponse.status_code, 200)
