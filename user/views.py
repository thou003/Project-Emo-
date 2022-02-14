
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입
        pass
        # email = request.data.get('email', None)
        # nickname = request.data.get('nickname', None)
        # name = request.data.get('name', None)
        # password = request.data.get('password', None)
        #
        # User.objects.create(email=email,
        #                     nickname=nickname,
        #                     name=name,
        #                     password=make_password(password),
        #                     profile_image="default_profile.jpg")
        # return Response(status=200)