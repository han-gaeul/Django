from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')

    else:
        article_form = ArticleForm()
    
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/new.html', context=context)