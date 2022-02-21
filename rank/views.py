from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from django.db import connection
from django.http import JsonResponse
from django.http import HttpResponse
import json


def Data2(request):
    # POST 요청일 때

    if request.method == 'POST':

        post = json.loads(request.body)
        print(post)
        if post is None:
            post = ""

        cursor = connection.cursor()

        strSql = "select id, service, title, img, artist, price, sell, likes from searchrank " + post

        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        ranks = []

        for data in datas:
            row = {'id': data[0],
                   'service': data[1],
                   'title': data[2],
                   'img': data[3],
                   'artist': data[4],
                   'price': data[5],
                   'sell': data[6],
                   'likes': data[7]
                   }

            ranks.append(row)

        #context = {"data": ranks}
    return HttpResponse(json.dumps(ranks))
    #return HttpResponse(ranks)



class Rank(APIView):
    def get(self, request):
        return render(request, "rank/rank.html")

class Detail(APIView):
    def get(self, request):
        return render(request, "rank/detail.html")

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")