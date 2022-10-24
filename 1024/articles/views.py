from django.shortcuts import render
from .models import Article

# Create your views here.

# 글 목록
def index(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article' : article
    }
    return render(request, 'article/index.html', context)