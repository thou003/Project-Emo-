import os

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.response import Response

from .models import Member
# Create your views here.
from rest_framework.views import APIView


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email', None)
        #nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        birth = request.data.get('birth', None)
        phonenumber = request.data.get('phonenumber', None)

        Member.objects.create(email=email,
                            name=name,
                            password=password,
                            birth=birth,
                            phonenumber=phonenumber)

        return Response(status=200)

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")


class Mypage(APIView):
    def get(self, request):
        return render(request, "user/mypage.html")