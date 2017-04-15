from django.shortcuts import render

# from django.http import HttpResponse
from post.models import Post

def homepage(request):
    allposts = Post.objects.all()
    context = {"name": "Yoyo",
                "day": "Friday",
                "posts": allposts}

    return render(request, "index.html", context)
    # return HttpResponse("Hello World")
