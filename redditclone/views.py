from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    #render(request, "index.html")
    return HttpResponse("Hello World")
