from .views import Join, Login, Mypage
from django.urls import path

urlpatterns = [
    path('join/', Join.as_view()),
    path('login/', Login.as_view()),
    path('mypage/', Mypage.as_view())
]