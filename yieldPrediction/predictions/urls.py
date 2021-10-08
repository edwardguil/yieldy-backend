from django.urls import path
from .views import PredictionView

# The endpoints for this APP.
urlpatterns = [
    path('', PredictionView.as_view()),
]
