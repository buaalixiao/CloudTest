from django.http import HttpResponse,Http404
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def test(request,page):
    htmlReturn = page+'.html'
    return render(request,htmlReturn)