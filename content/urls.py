from .views import Rank
from django.urls import path

urlpatterns = [
    path('rank/', Rank.as_view()),
]