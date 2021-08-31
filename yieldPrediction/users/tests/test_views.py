from users.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from users.views import GetUserView, UserView




class TestUserView(APITestCase):

    def inital_setup(self):
        self.userView = UserView.as_view()
        self.factory = APIRequestFactory()

    def testInvalidEmail(self):
        self.inital_setup()
        request = self.factory.post('/user/', {'email': 'test', 'password' : '123dsfsdf'})
        response = self.userView(request)
        assert response.status_code == 400
        print(response.data)

    def testValidEmail(self):
        assert 1 == 2



