from django.urls import path
from .views import UserView#, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', UserView.as_view())
]
