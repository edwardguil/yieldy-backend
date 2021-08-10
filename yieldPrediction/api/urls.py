from django.urls import path
from .views import UserModelView

urlpatterns = [
    path('', UserModelView.as_view())
]
