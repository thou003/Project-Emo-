from django.db.models import Q
from django.shortcuts import render
from django.views.generic import FormView
from rest_framework import request
from rest_framework.views import APIView

from .forms import EmoticonSearchForm
from .models import Emoticon

# Create your views here.

class Search(FormView):
    form_class = EmoticonSearchForm
    template_name = 'search/search.html'

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


# class Result(APIView):
#
# class Result(APIView):
#     def post(self, request):
#         search = request.data.get('search')
#
#         results = Emoticon.objects.filter(
#             Q(service=search) | Q(artist=search) | Q(title=search) | Q(tag=search)
#         )
#         context = {'search': search, 'results': results}
#
#         return render(request, "search/result.html", context=context)

#
# def search(request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         results = Emoticon.objects.filter(
#             Q(service=search) | Q(artist=search) | Q(title=search) | Q(tag=search)
#         )
#         context = {'search': search, 'results': results}
#         return render(request, 'search/result.html', context=context)
#     else:
#         return render(request, 'search/result.html', {})

class SearchFormView(FormView):
    form_class = EmoticonSearchForm
    template_name = 'search/search.html'

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
