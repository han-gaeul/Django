from django import forms
from .models import Review
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'palceholder' : '제목을 입력해주세요.'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'palceholder' : '내용을 입력해주세요.'
                }
            )
        }