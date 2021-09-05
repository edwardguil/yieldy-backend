from django.urls import path
from .views import PaddockView, DeletePaddockView

urlpatterns = [
    path('', PaddockView.as_view(), name="createPaddock"),
    path('/<int:idPaddock>', DeletePaddockView.as_view(), name="deletePaddock"),
]
