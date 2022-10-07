from django.shortcuts import render

# Create your views here.

def index(reqeust):
    return render(reqeust, 'articles/index.html')