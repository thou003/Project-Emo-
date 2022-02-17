from .views import Rank, Main, emoticon
from django.urls import path

urlpatterns = [
    path('rank/', Rank.as_view()),
    path('emoticon/', emoticon.as_view())
]