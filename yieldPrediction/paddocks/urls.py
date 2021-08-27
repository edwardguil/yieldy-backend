from django.urls import path
from .views import PaddockView, DeletePaddockView

urlpatterns = [
    path('', PaddockView.as_view()),
    path('<int:id>', DeletePaddockView.as_view()),
]
