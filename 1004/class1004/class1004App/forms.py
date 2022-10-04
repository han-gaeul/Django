from statistics import mode
from django import forms
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Meta 클래스는 내부 클래스로 활용되며
    # 이는 기본 필드의 값을 재정의 할 때 사용
    # 즉, Article로부터 모델을 가져오고
    # 그 중 'title', 'content'를 가져온다는 의미
    class Meta:
        model = Article
        fields = ['title', 'content']