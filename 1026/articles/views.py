from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_safe

# Create your views here.

# 글 목록
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# 글 조회
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
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
    article = get_object_or_404(Article, pk=pk)
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

# 리뷰 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    context = {
        'article' : article
    }
    return render(request, 'articles/index.html', context)

# 댓글 작성
@login_required
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
        return JsonResponse(context)

# 댓글 삭제
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', pk)

# 좋아요
@login_required
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.like_users.all(): 
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)