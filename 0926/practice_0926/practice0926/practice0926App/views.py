from django.shortcuts import render
import random

# Create your views here.

# def is_odd_even(request, _number):
#     context = {
#         'number' : _number,           
#     }
#     return render(request, 'is_odd_even.html', context)

def index(request):
    return render(request, "index.html")


def previous_life(request):
    return render(request, "previous-life.html")


def is_odd_even(request, id):

    if id % 2 == 0 and id != 0:
        res = "짝수"
    elif id % 2 == 1:
        res = "홀수"
    else:
        res = '0'

    context = {"res": res, "id": id}

    return render(request, "is_odd_even.html", context)


def calculator(request, num1, num2):

    if num2 == 0:
        return render(request, "error.html")

    res_sum = num1 + num2
    res_sub = num1 - num2
    res_mul = num1 * num2
    res_div = num1 // num2

    context = {
        "sum": res_sum,
        "sub": res_sub,
        "mul": res_mul,
        "div": res_div,
        "num1": num1,
        "num2": num2,
    }

    return render(request, "calculator.html", context)


def previous_life_result(request):
    name = request.GET.get("name")
    prevs = ["왕", "선비", "거지"]
    imgs = {
        "왕": "https://www.resizepixel.com/Image/fz2r1e15o4/Preview/20181228135812_1286269_667_1000.jpg?v=a6826762-6076-4c53-bb28-8db10cfc1b65",
        "선비": "https://www.resizepixel.com/Image/4e426qhd2z/Preview/04.jpg?v=38988b19-d156-47e0-b173-bf82f09f5409",
        "거지": "https://www.resizepixel.com/Image/osftzp72cs/Preview/20100318000824_r.jpg?v=c9eb55b3-d795-464c-b0e2-2405f193c2fa",
    }

    prev = random.choice(prevs)
    context = {
        "name": name,
        "before": prev,
        "img": imgs.get(prev)
    }

    return render(request, "previous-life-result.html", context)


def lorem(request):
    return render(request, "lorem.html")


def lorem_result(request):
    cnt_number = int(request.GET.get("number"))
    cnt_words = int(request.GET.get("words"))

    lorems = [[] for _ in range(cnt_number)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "lorem-result.html", context)