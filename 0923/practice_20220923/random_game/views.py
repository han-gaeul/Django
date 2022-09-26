from django.shortcuts import render
import random

# Create your views here.

# view -> 템플릿 파일 지정
def index(request):

    return render(request, 'index.html')

def today_beer(request):
    beer_list = [
        {'name' : '에델바이스', 'src' : 'https://ppss.kr/wp-content/uploads/2021/07/1-10.jpg'},
        {'name' : '테라', 'src' : 'https://img.hankyung.com/photo/201905/AKR20190502080000030_01_i.jpg'},
        {'name' : '호가든', 'src' : 'https://image.newdaily.co.kr/site/data/img/2020/07/07/2020070700095_0.jpg'},
    ]
    beer = random.choice(beer_list)
    context = {
        'beer' : beer
    }
    return render(request, 'today_beer.html', context)

def lotto(request):
    # 로또 번호 6개를 5번 뽑기
    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range(1, 46), 6)
        lotto_list.append(lotto)

    context = {
        'lotto_list' : lotto_list,
    }
    return render(request, 'lotto.html', context)