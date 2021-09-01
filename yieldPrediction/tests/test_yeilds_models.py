from datetime import date
from django.test import TestCase
from yields.models import Yield
from users.models import User
from paddocks.models import Paddock, Crop
from yieldModels.BasicModel import basicModel, grainWeight

class YieldTest(TestCase):
    def setUp(self) -> None:
        Crop.objects.create(name="Wheet")
        User.objects.create(email = "test@test.com")
        self.crop = Crop.objects.get(name="Wheet")
        self.user = User.objects.get(email = 'test@test.com')
        Paddock.objects.create(
            user = self.user,
            cropType = self.crop,
            name = "Test Paddock",
            size_ha = 120,
            rowSpacing_cm = 17.5,
            location = 0,
            grainsPerHead = 120,
            headsPerM2 = 50)
        self.paddock = Paddock.objects.get(name="Test Paddock")
        self.harvest_t = basicModel(self.paddock.grainsPerHead, self.paddock.headsPerM2/4, grainWeight[5][1])
        Yield.objects.create(
            user = self.user,
            paddock = self.paddock,
            harvest_t = self.harvest_t,
            date = "2021-01-01")
        self.yields = Yield.objects.get(user = self.user)


    def test_yield_user(self):
        self.assertEquals(self.yields.user, self.user)

    def test_yield_paddock(self):
        self.assertEquals(self.yields.user, self.user)

    def test_yield_harvest_t(self):
        self.assertEquals(self.yields.harvest_t, self.harvest_t)

    def test_yield_date(self):
        self.assertEquals(self.yields.date, date(2021,1,1))