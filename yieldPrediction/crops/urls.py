from django.urls import path
from .views import CropView
#from .views import

urlpatterns = [
    path('', CropView.as_view()),
]
