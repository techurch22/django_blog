from .views import show_all_video, show_film
from django.urls import path

urlpatterns = [
    path('', show_all_video ),
    path('movie/<str:slug>', show_film, name='filming')
]