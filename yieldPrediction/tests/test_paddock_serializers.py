from django.test import TestCase
from paddocks.models import Paddock, Crop
from paddocks.serializers import PaddockSerializer
from users.models import User

class PaddockSerializerTest(TestCase):
    def setUp(self):
        User.objects.create(email = "test@test.com")
        Crop.objects.create(name = "Wheat")
        self.crop = Crop.objects.get(name="Wheat")
        self.user = User.objects.get(email = "test@test.com")
        Paddock.objects.create(
            user = self.user,
            cropType = self.crop,
            name = "Test Paddock",
            size_ha = 120,
            rowSpacing_cm = 17.5,
            location = 0,
            grainsPerHead = 120,
            headsPerM2 = 50)
        self.serializer = PaddockSerializer()

    def test_paddock_serializer(self):
        print(self.serializer.get_paddocks())