from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from search.forms import EmoticonSearchForm
from .models import Emoticon
from rest_framework.views import APIView
from django.views.generic import DeleteView, FormView
from rest_framework.response import Response

# 인기페이지
class Rank(APIView):
    def get(self, request):
        return render(request, "content/rank.html")

# 메인
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


# 인기페이지
class Recommend(APIView):
    def get(self, request):
        return render(request, "content/recommend.html")

# 신규페이지
class New(APIView):
    def get(self, request):

        page = request.GET.get('page', '1') #페이지

        newdatas = Emoticon.objects.all().order_by('id')

        paginator = Paginator(newdatas, 12) #페이지당 12개
        page_obj = paginator.get_page(page)

        context = {'newdatas':page_obj}
        return render(request, "content/new_new.html", context)