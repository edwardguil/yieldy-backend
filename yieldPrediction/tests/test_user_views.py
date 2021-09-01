from django.http import request
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from users.views import UserView, GetUserView
from users.models import User
from users.authFunctions import validate_token, refresh_token

class UserTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.postView = UserView.as_view()
        self.getView = GetUserView.as_view()
        self.userData = {'email': 'test@test.com', 'password': 'testpassword'}
        #self.testUser = User.objects.create(email = 'test@test.com', password = 'testpassword')
        #self.testUser.is_active = True
        #self.testUser.save()

    def test_post_content(self):
        request = self.factory.post('/user/', data = self.userData)
        response = self.view(request)
        self.assertEquals(response.data, 'test@test.com') #['user']['email']
        self.assertEquals(response.status_code, 0)

    def test_get_content(self):
        postRequest = self.factory.post('/user/', data = self.userData)
        postResponse = self.postView(postRequest)
        self.assertEquals(postResponse.data, 401)
        getRequest = self.factory.get(f'/user/{postResponse.data["user"]["id"]}/')
        getResponse = self.getView(getRequest)
        self.assertEquals(getResponse.status_code, 0)