from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Post

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def posts(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

def post(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404

    context = {
        'post': post
    }
    return render(request, 'post.html',context)