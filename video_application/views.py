from video_application.models import Video
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Avg, Min, Max, Count, Value


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
