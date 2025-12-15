from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from . models import Post

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def posts(request):
    post_list = Post.published_posts.all()
    context = {
        'posts': post_list
    }
    return render(request, 'blog/list.html', context)

def post(request, id):
    detail = get_object_or_404(Post, id=id, status= Post.Status.PUBLISHED)
   # try:
   #     detail = Post.published_posts.get(id=id)
   # except:
   #     raise Http404

    context = {
        'post': detail
    }
    return render(request, 'blog/detail.html',context)