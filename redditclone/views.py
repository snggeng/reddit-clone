from django.shortcuts import render

from post.models import Post

def homepage(request):
    allposts = Post.objects.order_by('-score')
    context = {"name": "Geng",
                "day": "Friday",
                "posts": allposts}

    return render(request, "index.html", context)
