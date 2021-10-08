from django.urls import path
from .views import YieldView

# The endpoints for the API & browsable interface.
urlpatterns = [
    path('', YieldView.as_view()),
]
