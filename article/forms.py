from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary','published_date', 'author', 'content',  'image']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'summary': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 7})
        }
