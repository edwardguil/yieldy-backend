#from rest_framework.test import APITestCase
from .test_setup import TestSetUp
from django.urls import reverse


from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})

class TestPaddockViews(TestSetUp):
        
    def test_create(self):
        response = self.client.post(path = reverse('createPaddock'),data=self.paddockData, format='json')
        self.assertEquals(response.status_code, "400")