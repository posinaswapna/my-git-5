from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>my first app and string response</h1>')

    def second(request):
         return HttpResponse('<h1>my first app and string two response</h1>')