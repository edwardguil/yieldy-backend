from rest_framework.test import APIRequestFactory
from django.test import TestCase
from users.views import UserView, GetUserView

class UserTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.userData = {'email': 'test@test.com', 'password': 'testpassword'}

    def test_post_content(self):
        request = self.factory.post('/user/', data = self.userData)
        response = UserView.as_view()(request)

        self.assertEquals(response.data['user']['email'], 'test@test.com')
        self.assertEquals(response.status_code, 202)

    def test_get_content(self):
        postRequest = self.factory.post('/user/', data = self.userData)
        postResponse = UserView.as_view()(postRequest)
        ID = postResponse.data["user"]["id"]

        getRequest = self.factory.get(f'/user/{ID}')
        getResponse = GetUserView.as_view()(getRequest, idUser=ID, authed=True)

        self.assertEquals(getResponse.status_code, 200)