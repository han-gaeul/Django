from django.shortcuts import redirect, render
from .models import Movie
from .form import MovieForm

# Create your views here.

# 영화 데이터 목록 조회
def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/movies.html', context)

# 영화 데이터 정보 조회
def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies' : movies
    }
    return render(request, 'movies/detail.html', context)

# 영화 데이터 생성
def create(request):
    if request.method == 'POST':
        movies_form = MovieForm(request.POST)
        
        if movies_form.is_valid():
            movies_form.save()
            return redirect('movie:movies')
    
    else:
        movies_form = MovieForm()
    
    context = {
        'movies_form' : movies_form
    }
    return render(request, 'movies/create.html', context=context)

# 영화 데이터 수정
def update(request, pk):
    movie = Movie.objects.get()
    return render(request, 'movies/update.html')

# 영화 데이터 삭제
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movies:movie')