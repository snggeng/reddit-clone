from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    context = {"name": "Yoyo",
                "day": "Friday"}
    return render(request, "index.html", context)
    # return HttpResponse("Hello World")
