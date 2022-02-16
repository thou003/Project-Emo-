from .views import Join, Login, Mypage, Edituser, Updateuser
from django.urls import path

urlpatterns = [
    path('join/', Join.as_view()),
    path('login/', Login.as_view()),
    path('mypage/', Mypage.as_view()),
    path('edituser/', Edituser.as_view()),
    path('update/', Updateuser.as_view())
]