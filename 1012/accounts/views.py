from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def accounts(request):
    accounts = get_user_model().objects.order_by('pk')
    context = {
        'accounts' : accounts
    }
    return render(request, 'accounts/accounts.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/detail.html', context)

def sign(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아님
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                # 세션에 저장
                # login 함수는 request, user 객체를 인자로 받음
                # user 객체는 form에서 인증된 우저 정보를 받을 수 있음
                auth_login(request, form.get_user())
                return redirect('articles:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)