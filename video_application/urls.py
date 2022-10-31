from .views import *
from django.urls import path

urlpatterns = [
    path('', show_all_video, name='all_films'),
    path('movie/<str:slug>', show_film, name='filming'),
    path('director/', show_all_directors, name='all_director'),
    path('director/<str:slug>', show_director, name='director'),
    path('actors/', show_all_actors, name='actors'),
    path('actors/<str:slug>', show_actor, name='actor'),
    path('newfilm', new_film, name='newfilm'),
    path('movie/<str:slug>/edit', edit_film, name='edit_film'),
    path('movie/<str:slug>/delete', delete_film, name='delete_film')

]