from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    # 모든 글 목록을 보여줌
    # DB에서 모든 글을 불러옴
    posts = Post.objects.all()

    # template에 보냄
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    # parameter로 날아온 데이터를 받아서 
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    Post.objects.create(title=title, content=content)

    context = {
        'title' : title,
        'content' : content,
    }
    return redirect('posts:index')

def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')