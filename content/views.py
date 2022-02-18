from django.db.models import Q
from django.shortcuts import render

from search.forms import EmoticonSearchForm
from .models import Emoticon
# Create your views here.
from rest_framework.views import APIView

from django.views.generic import DeleteView, FormView
from rest_framework.response import Response

class Rank(APIView):
    def get(self, request):
        return render(request, "content/rank.html")


class Main(FormView):
    form_class = EmoticonSearchForm
    template_name = 'emoshop/main.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        emoticon_list = Emoticon.objects.filter(
            Q(title__icontains=searchWord) |
            Q(artist__icontains=searchWord) |
            Q(service__icontains=searchWord)
        )
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = emoticon_list

        return render(self.request, self.template_name, context)


class emoticon(APIView):
    def get(self, request):
        emoticons = Emoticon.objects.filter(service='kakao')
        context = {'emoticons': emoticons}

        return render(request, "content/rank.html", context=context)

class Recommend(APIView):
    def get(self, request):
        return render(request, "content/recommend.html")
