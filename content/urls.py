from .views import Rank, Main
from django.urls import path

urlpatterns = [
    path('rank/', Rank.as_view()),
]