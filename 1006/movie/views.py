from django.shortcuts import redirect, render
from .models import Movie

# Create your views here.

# 영화 데이터 목록 조회
def movies(request):
    return render(request, 'movies/movies.html')

# 영화 데이터 정보 조회
def detail(request, pk):
    return render(request, 'movies/detail.html')

# 영화 데이터 생성
def create(request):
    return render(request, 'movies/create.html')

# 영화 데이터 수정
def update(request, pk):
    return render(request, 'movies/update.html')

# 영화 데이터 삭제
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movies:movie')