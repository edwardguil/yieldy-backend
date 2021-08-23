from django.urls import path
from .views import UserView, GetUserView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:id>', GetUserView.as_view())
]

