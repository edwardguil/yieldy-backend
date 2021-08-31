from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):

    def setup(self):
        self.createUrl = reverse('createPaddock')
        self.deleteUrl = reverse('deletePaddock')
        
        self.paddockData = {
            "name" : "Test Paddock",
            "size_ha" : 120,
            "rowSpacing_cm" : 17.5,
            "cropType" : "Wheat"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
