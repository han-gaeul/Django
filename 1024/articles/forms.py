from django import forms
from .models import Comment, Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user', )