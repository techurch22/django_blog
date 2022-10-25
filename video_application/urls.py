from .views import show_all_video, show_film, show_director, show_all_directors
from django.urls import path

urlpatterns = [
    path('', show_all_video ),
    path('movie/<str:slug>', show_film, name='filming'),
    path('director/', show_all_directors, name='all_director'),
    path('director/<str:slug>', show_director, name='director'),

]