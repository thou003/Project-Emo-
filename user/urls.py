from .views import Join
from django.urls import path

urlpatterns = [
    path('join/', Join.as_view()),
]
