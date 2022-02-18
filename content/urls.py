from .views import emoticon, Recommend
from django.urls import path

urlpatterns = [
    path('rank/', emoticon.as_view()),
    path('recommend/', Recommend.as_view()) # 127.0.0.1:8000/content/recommend
]