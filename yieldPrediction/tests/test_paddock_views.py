from django.http import request, response
from paddocks.models import Paddock
from rest_framework.test import APIRequestFactory, APITestCase
from paddocks.views import PaddockView, DeletePaddockView
from users.views import UserView, GetUserView


class PaddockViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.paddockView = PaddockView.as_view()
        self.paddockData = {
            'name': 'test paddock',
            'size_ha': 120,
            'rowSpacing_cm': 17.5,
            'cropType': 'Wheat'
            }
        self.userData = {
            'email': 'test@test.com', 
            'password': 'testpassword'
            }

    def test_paddock_post(self):
        userRes = self.client.post('/user/', self.userData)
        #userRes = UserView.as_view()(userReq)

        ID = userRes.data["user"]["id"]
        self.assertEquals(userRes.status_code, 202)

        paddockRequest = self.client.post(f'/user/{ID}/paddock', data = self.paddockData)
        #paddockReponse = PaddockView.as_view()(request = paddockRequest,  idUser = ID, authed = True)
        self.assertEquals(paddockRequest.data, 0)