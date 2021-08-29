from django.urls import path
from .views import YieldView

urlpatterns = [
    path('', YieldView.as_view()),
    #path('<int:idYield>', view.as_view()),
]
