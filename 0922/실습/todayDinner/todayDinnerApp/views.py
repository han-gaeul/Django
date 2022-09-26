from random import random
from django.shortcuts import render

# Create your views here.

def todayDinner(request):
    food_list = ['삼겹살', '치즈돈가스', '파스타', '초밥', '아구찜']
    food = random.choice(food_list)
    image_list = [
        'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg',
        'http://th4.tmon.kr/thumbs/image/adb/b40/1d6/0fabab3f3_700x700_95_FIT.jpg',
        'https://images.chosun.com/resizer/wsSVlD2KlkIAXTYSWUZxQSceAUE=/960x504/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HS2MWHN32OMYMSDYNGYRIZCXNI.jpg',
        'https://hajl.athuman.com/karuta/uploads/6e45128aad8bdcf39055b81840ecbe0186605633.jpeg',
        'https://recipe1.ezmember.co.kr/cache/recipe/2021/08/05/98998b80a8bba88b91b8829417f416a61.jpg',
    ]
    image = random.choice(image_list)
    context = {
        'food' : food,
        'images' : image,
    }
    return render(request, 'todayDinner.html', context)