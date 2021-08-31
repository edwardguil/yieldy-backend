#from rest_framework.test import APITestCase
from .test_setup import TestSetUp
from django.urls import reverse
from rest_framework.test import RequestsClient


client = RequestsClient()
response = client.get('http://127.0.0.1:8000')
assert response.status_code == 200


class TestPaddockViews(TestSetUp):
        
    def test_create(self):
        response = self.client.post(path=reverse("createPaddock"), data={
            "name" : "Test Paddock",
            "size_ha" : 120,
            "rowSpacing_cm" : 17.5,
            "cropType" : "Wheat"
        }, format='json')
        self.assertEquals(response.status_code, "200")