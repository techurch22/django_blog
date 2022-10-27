from django import forms
from .models import Video
from .models import Director


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'rating', 'year', 'budget', 'director', 'actors']


        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'placeholder': "Название картины",
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "rating",
                'placeholder': "Рейтинг"
            }),
            'year': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "year",
                'placeholder': "Год выхода"
            }),
            'budget': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "budget",
                'placeholder': "Бюджет"
            }),
            'director': forms.Select(attrs={
                'class': "form-control",
                'id': "director",
                'placeholder': "Режисер"
            }),
            'actors': forms.SelectMultiple(attrs={
                'class': "form-control",
                'id': "actors",
                'placeholder': "Актеры"
            }),
        }

