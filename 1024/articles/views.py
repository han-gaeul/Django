from django.shortcuts import render

from articles.forms import CommentForm
from .models import Article

# Create your views here.

# 글 목록
def index(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article' : article
    }
    return render(request, 'article/index.html', context)

# 글 조회
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : article.comment_set.all(),
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)