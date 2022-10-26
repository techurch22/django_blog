from video_application.models import Video, Director, Actor
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Count


def show_all_directors(request):
    context = Director.objects.all()
    return render(request, 'video_application/all_directors.html', context={
        'context': context
    })

def show_all_video(request):
    context = Video.objects.order_by(F('rating').desc())
    aggregator = context.aggregate(Count('id'))
    return render(request, 'video_application/all_films.html', context={
        'context': context,
        'aggregator': aggregator,
    })


def show_film(request, slug):
    context = get_object_or_404(Video, slug=slug)
    return render(request, 'video_application/film.html', context={
        'context': context
    })

def show_director(request, slug):
    director = get_object_or_404(Director, direct_slug=slug)
    films = Video.objects.filter(director=director)
    return render(request, 'video_application/director.html', context={
        'director': director,
        'films': films
    })

def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'video_application/all_actors.html', context={
        'actors': actors
    })

def show_actor(request, slug):
    actor = get_object_or_404(Actor, actor_slug=slug)
    films = actor.videos.all()
    return render(request, 'video_application/actor.html', context={
        'actor': actor,
        'films': films
    })