from django.shortcuts import redirect, render
from forms import ArticleForm, CommentForm
from .models import Article
from django.contrib.auth.decorators import login_required

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

# 글 작성
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)

# 리뷰 수정
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)