from django.urls import path
from .views import YieldView

urlpatterns = [
    path('', YieldView.as_view()),
]
