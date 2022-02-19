from . import views
from .views import Join, Login, Mypage, Edituser, Updateuser, Purchase
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('join/', Join.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('mypage/', Mypage.as_view(), name='mypage'),
    path('edituser/', Edituser.as_view()),
    path('update/', Updateuser.as_view()),
    path('quit/', views.deleteuser, name='quitmember'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('purchase/', Purchase.as_view(), name='purchase')
]