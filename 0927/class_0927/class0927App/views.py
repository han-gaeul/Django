from django.shortcuts import render
from .models import articles

# Create your views here.

# guestbook = []

def index(request):
    # DB에서 가져오기
    guestbook = articles.objects.all()
    # SELECT * FROM articles:
    return render(request, 'class/index.html', {'guestbook' : guestbook})

def create(request):
    content = request.GET.get('content')
    # guestbook.append(content)
    # DB에 저장
    articles.objects.create(content=content)
    return render(request, 'class/create.html', {'content' : content})