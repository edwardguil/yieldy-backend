from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/user/', {'username': 'testuser', 'password' : 'testpassword'})