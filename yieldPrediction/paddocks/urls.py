from django.urls import path
from .views import PaddockView

urlpatterns = [
    path('', PaddockView.as_view())
]
