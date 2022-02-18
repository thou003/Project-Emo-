from django import forms
from django.http import HttpResponse, HttpResponseRedirect

class EmoticonSearchForm(forms.Form):
    search_word = forms.CharField(label="")