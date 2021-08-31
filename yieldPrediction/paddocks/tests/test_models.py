from django.test import TestCase
from paddocks.models import Crop, Paddock
from users.models import User

class CropTest(TestCase):
    def setUp(self) -> None:
        Crop.objects.create(name="Wheat")

    def test_crop_name(self):
        name = Crop.objects.get(name="Wheat")
        self.assertEquals(name.name, "Wheat")

class PaddockTest(TestCase):
    def setUp(self) -> None:
        Crop.objects.create(name = "Wheat")
        self.crop = Crop.objects.get(name="Wheat")
        self.user = User.objects.create(email = "test@test.com")
        Paddock.objects.create(
            user = self.user,
            cropType = self.crop,
            name = "Test Paddock",
            size_ha = 2,
            rowSpacing_cm = 17.5,
            location = 0,
            grainsPerHead = 120,
            headsPerM2 = 50)
        self.paddock = Paddock.objects.get(name = "Test Paddock")

    def test_paddock_user(self):
        self.assertEquals(self.paddock.user, self.user)
    
    def test_paddock_cropType(self):
        self.assertEquals(self.paddock.cropType, self.crop)
    
    def test_paddock_name(self):
        self.assertEquals(self.paddock.name, "Test Paddock")
    
    def test_paddock_size_ha(self):
        self.assertEquals(self.paddock.size_ha, 2)
    
    def test_paddock_rowSpacing_cm(self):
        self.assertEquals(self.paddock.rowSpacing_cm, 17.5)
    
    def test_paddock_location(self):
        self.assertEquals(self.paddock.location, 0)
    
    def test_paddock_grainsPerHead(self):
        self.assertEquals(self.paddock.grainsPerHead, 120)
    
    def test_paddock_headsPerM2(self):
        self.assertEquals(self.paddock.headsPerM2, 50)