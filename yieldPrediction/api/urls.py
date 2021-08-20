from django.urls import path
from .views import UserModelView, CreateUserModel

urlpatterns = [
    path('GetUserModel/', UserModelView.as_view()),
]