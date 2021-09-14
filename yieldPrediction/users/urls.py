from django.urls import path
from .views import LoginUserView, RegisterUserView, GetUserView

urlpatterns = [
    path('login', LoginUserView.as_view()),
    path('register', RegisterUserView.as_view()),
    path('<int:idUser>', GetUserView.as_view())
]

