from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class Rank(APIView):
    def get(self, request):
        return render(request, "content/rank.html")