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
        # id = request.data.get('id', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        birth = request.data.get('birth', None)
        phonenumber = request.data.get('phonenumber', None)
        gender = request.data.get('gender', None)
        member_type = request.data.get('member_type', None)
        id = request.data.get('id', None)

        Member.objects.create(email=email,
                            sex=gender,
                            name=name,
                            password=password,
                            birth=birth,
                            phonenumber=phonenumber,
                            type=member_type,
                            id=id)

        return Response(status=200)

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html/")

    def post(self, request):
        # TODO 로그인
        id = request.data.get('id', None)
        password = request.data.get('password', None)

        user = Member.objects.filter(id=id).first()

        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

        if user.password==password:
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['id'] = id
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


class Mypage(APIView):
    def get(self, request):
        return render(request, "user/mypage.html")