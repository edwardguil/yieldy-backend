from django.http import request
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from users.views import UserView

factory = APIRequestFactory()


class UserTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = UserView.as_view()
        self.userData = {'email': 'test@test.com', 'password' : 'testpassword'}

    def test_post_content(self):
        request = factory.post('/user/', data = self.userData)
        response = self.view(request)
        self.assertEquals(response.data['user']['email'], 'test@test.com')
        self.assertEquals(response.status_code, 202)

    def test_get_content(self):
        postRequest = factory.post('/user/', data = self.userData)
        postResponse = self.view(postRequest)
        self.assertEquals(postResponse.status_code, 202)
        getRequest = factory.get(f'/user/{postResponse.data["user"]["id"]}/')
        getResponse = self.view(getRequest)
        self.assertEquals(getResponse.data, 202)