
from django.contrib import admin
from django.urls import path, include
from content.views import Main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('user/', include('user.urls')),
    path('content/', include('content.urls')),
    path('search/', include('search.urls')),
]
