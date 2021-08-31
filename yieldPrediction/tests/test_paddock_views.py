from django.http import request, response
from yieldPrediction.paddocks.models import Paddock
from yieldPrediction.paddocks.views import DeletePaddockView
from rest_framework.test import APIRequestFactory, APITestCase
from paddocks.views import PaddockView, DeletePaddockView


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
        userReq = self.factory.post('/user/', self.userData)
        userRes = self.view(userReq)
        paddockRequest = self.factory.post(f'/user/{userRes.data["user"]["id"]}/paddock', self.paddockData)
        paddockReponse = self.view(paddockRequest)
        self.assertEquals(paddockReponse, 0)

