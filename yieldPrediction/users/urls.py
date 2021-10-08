from django.urls import path
from .views import UserView, GetUserView

# The endpoints for the API & browsable interface.
urlpatterns = [
    path('', UserView.as_view()),
    path('/<int:idUser>', GetUserView.as_view())
]

