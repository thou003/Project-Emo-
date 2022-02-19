from .views import Rank, Main, emoticon, Recommend, New
from django.urls import path

app_name = 'new'

urlpatterns = [
    path('rank/', emoticon.as_view()),
    path('recommend/', Recommend.as_view(), name='recommed'),
    path('new/', New.as_view(), name='new')

    # path('emoticon/', emoticon.as_view())
]