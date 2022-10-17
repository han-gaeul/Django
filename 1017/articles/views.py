from django.shortcuts import render

# Create your views here.
# 목록 조회
def index(request):
    return render(request, 'articles/index.html')

# 정보 조회
def detail(request, pk):
    return render(request, 'articles/detail.html')

# 생성
def create(request):
    return render(request, 'articles/new.html')

# 수정
def update(request, pk):
    return render(request, 'articles/update.html')

# 삭제
def delete(request):
    return render()