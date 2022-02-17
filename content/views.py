from django.shortcuts import render
from .models import emoticon
# Create your views here.
from rest_framework.views import APIView

from django.views.generic import DeleteView
from rest_framework.response import Response


class Rank(APIView):
    def get(self, request):
        return render(request, "content/rank.html")

class Main(APIView):
    def get(self, request):
        return render(request, "emoshop/main.html")

class emoticon(APIView):

    def get(self, request):

        emoticons = emoticon.objects.filter(service=kakao)

        return render(request, "content/rank.html", context=context)
