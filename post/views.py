# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from forms import PostForm
from models import Post

import json
# Create your views here.

# Post creation utilities

def createpost(request):
    return render_form(request, "createpost.html", "post/create", PostForm)

def upvote(request, pid="2"):
    try:
        post = Post.objects.get(id=int(pid))
        post.score += 1
        post.save()
        return HttpResponse(post.score)
    except Exception:
       return HttpResponseNotFound("Could not find post with id " + pid)

def generate_form_context(form, is_form, action, old_context={}):
    old_context['form'] = form
    old_context['is_form'] = is_form
    old_context['action'] = action
    return old_context


def render_form(request, template, action, form_type, old_context={}):
    is_form = True
    if request.method == 'POST':
        form = form_type(request.POST)
        if form.is_valid():
            is_form = False
            form.save()
    else:
        form = form_type()
    return render(request, template, generate_form_context(form, is_form, action, old_context=old_context))
