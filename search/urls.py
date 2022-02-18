
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import Search

app_name = 'search'

urlpatterns = [
        path('', Search.as_view()),
        path('search/', views.SearchFormView.as_view(), name='search'),
]
