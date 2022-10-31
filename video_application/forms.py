from django import forms
from .models import Video
from .models import Director


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'rating', 'year', 'budget', 'director', 'actors']
        labels = {
            "name": "Название фильма",
            "rating": "Рейтинг",
            "year": "Год выхода",
            "budget": "Бюджет",
            "director": "Режиссер",
            "actors": "В ролях",
        }


        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'placeholder': "---",
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "rating",
                'placeholder': "---"
            }),
            'year': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "year",
                'placeholder': "---"
            }),
            'budget': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "budget",
                'placeholder': "---"
            }),
            'director': forms.Select(attrs={
                'class': "form-control",
                'id': "director",
                'placeholder': "---"
            }),
            'actors': forms.SelectMultiple(attrs={
                'class': "form-control",
                'id': "actors",
                'placeholder': "---"
            }),
        }

