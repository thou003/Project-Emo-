from .views import Rank, Data2, Detail
from django.urls import path
from . import views

app_name = 'rank'

urlpatterns = [

    path('rank/', Rank.as_view()),
    path('data2/', views.Data2, name='data2'),
    path('detail/', Detail.as_view()),
]