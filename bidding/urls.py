from django.urls import path
from .views import BidView

urlpatterns = [
    path('bid/', BidView.as_view(), name='bid')
]
