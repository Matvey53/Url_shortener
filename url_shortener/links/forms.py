from django import forms

from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ['original_url']
        labels = {
            'original_url': 'Введите ссылку',
        }
        widgets = {
            'original_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com'
            })
        }

