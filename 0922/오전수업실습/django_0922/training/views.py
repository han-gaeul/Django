import numbers
from django.shortcuts import render

# Create your views here.

# HTTP : 요청(request)을 하면 무언가를 응답(response)하는 방식
# index 함수 선언 및 정의
def index(request):
    return render(request, 'index.html')

def template(request):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    context = {
        'numbers' : number_list,
    }
    return render(request, 'template.html', context)