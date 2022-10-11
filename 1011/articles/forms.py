from dataclasses import field
from django import forms
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        field = ['title', 'content']