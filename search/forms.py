from django import forms
from django.http import HttpResponse, HttpResponseRedirect

class EmoticonSearchForm(forms.Form):
    search_word = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '이모티콘을 검색해보세요!'}))
