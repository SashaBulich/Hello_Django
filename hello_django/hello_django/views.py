from django.http import HttpResponse
from django.shortcuts import render
from django import forms


def about(request):
    a = 5 + 6
    return render(request, 'about.html',{'gretting' : a})

def home(request):
    return render(request, 'home.html')

# class New_form(forms.Form):
#     name = forms.CharField()
#     url = forms.URLField()
#     comment = forms.CharField(widget=forms.Textarea)
