from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    # 게시글 목록
    # 최근 작성한 글이 맨 위로 오게 정렬
    articles = Article.objects.order_by('-pk')
    # templates에 전달
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # Article.objects.create(title=title, content=content)

    if request.method == 'POST':
        # DB에 저장
        article_form = ArticleForm(request.POST)
        # is_valid() 메서드를 호출해 유효성 검증
        # 유효한지 아닌지에 따라 불리언 값 반환
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    # 특정 pk값의 글을 가져옴
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값을 가져와서 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)

        if article_form.is_valid():
            # 유효성 검사를 통과하면 저장하고 detail 페이지로
            article_form.save()
            redirect('articles:detail', article.pk)
    # 유효성 검사를 통과하지 못하면
    # context 부터 실행해서 오류 메시지가 담긴
    # article_form을 렌더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk).delete()
    return redirect('articles:index')