from django.urls import path
from .views import YieldView

# The endpoints for this APP.
urlpatterns = [
    path('', YieldView.as_view()),
]
