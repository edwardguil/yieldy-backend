from django.urls import path
from .views import UserView, GetUserView

# The endpoints for this APP.
urlpatterns = [
    path('', UserView.as_view()),
    path('/<int:idUser>', GetUserView.as_view())
]

