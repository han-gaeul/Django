from dataclasses import fields
from django import forms
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # all 이라고 하면 전체 필드를 추가
        fields = ['title', 'summary', 'running_time']