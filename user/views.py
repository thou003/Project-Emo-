import os

from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView
from rest_framework.response import Response
from .models import Member, Sell, Likes, Emoticon
# Create your views here.
from rest_framework.views import APIView


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html") # Join 들어오면 화면으로 여길 보여줘라!!

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        name = request.data.get('name')
        password = request.data.get('password')
        birth = request.data.get('birth')
        phonenumber = request.data.get('phonenumber')
        gender = request.data.get('gender')
        member_type = request.data.get('member_type')
        id = request.data.get('id')

        Member.objects.create(email=email,
                            sex=gender,
                            name=name,
                            password=password,
                            birth=birth,
                            phonenumber=phonenumber,
                            type=member_type,
                            id=id,
                            nickname=nickname)

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
        id = request.session.get('id', None)

        if id is None:
            return render(request, "user/login.html")

        user = Member.objects.filter(id=id).first()

        # ------구매내역 시작
        purchases = Sell.objects.filter(id=id).values('title')
        purchase_emoticons = Emoticon.objects.filter(title__in=purchases)
        # ------구매내역 끝

        # ------좋아요 시작
        likes = Likes.objects.filter(id=id).values('title')
        emoticons = Emoticon.objects.filter(title__in=likes)
        # ------좋아요 끝

        context = {'purchases': purchase_emoticons, 'emoticons': emoticons , 'user': user}

        if user is None:
            return render(request, "user/login.html")

        return render(request, 'user/mypage.html', context=context)

class Edituser(APIView):
    def get(self, request):
        id = request.session.get('id', None)
        user = Member.objects.filter(id=id).first()

        return render(request, 'user/edituser.html', context=dict(user=user))

class Updateuser(APIView):
    def post(self, request):
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        phonenumber = request.data.get('phonenumber')
        id = request.session.get('id')

        user = Member.objects.filter(id=id).first()

        user.password = password
        user.nickname = nickname
        user.phonenumber = phonenumber
        user.email = email
        user.save()

        return Response(status=200)


def deleteuser(request):
    id = request.session.get('id', None)
    user = Member.objects.get(id=id)
    user.delete()
    logout(request)

    return render(request, "emoshop/main.html")

class Purchase(APIView):
    def post(self, request):
        id = request.session.get('id', None)
        likes = Likes.objects.filter(id=id)

        for like in likes:
            Sell.objects.create(
                id=id,
                title=like.title,
                date=timezone.now(),
            )

        likes.delete()

        return redirect('user:mypage')

