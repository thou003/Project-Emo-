from .views import Rank, Main, emoticon
from django.urls import path

urlpatterns = [
    path('rank/', emoticon.as_view()),
    # path('emoticon/', emoticon.as_view())
]