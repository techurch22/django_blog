from django.contrib import admin
from .models import Video, Director, Actor
from django.db.models import QuerySet


# Register your models here.

class RatingFilter(admin.SimpleListFilter):
    title = 'rating'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('>70', 'Низкий'),
            ('>80', 'Средний'),
            ('>90', 'Высокий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '>70':
            return queryset.filter(rating__gte=70).filter(rating__lt=80)
        elif self.value() == '>80':
            return queryset.filter(rating__gte=80).filter(rating__lt=90)
        elif self.value() == '>90':
            return queryset.filter(rating__gte=90)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'direct_email']
    list_editable = ['first_name', 'last_name', 'direct_email']





class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'budget', 'rating', 'avg_budget_rating', 'cur_id', 'director']
    list_editable = ['year', 'budget', 'rating', 'cur_id', 'director']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['actors']
    ordering = ['-rating']
    actions = ['setup_usd', 'setup_eur', 'setup_rub']
    list_per_page = 10
    search_fields = ['name']
    list_filter = [RatingFilter]

    @admin.display(description='cost of [1] point rating')
    def avg_budget_rating(self, abr):
        return abr.budget // abr.rating

    @admin.action(description='Установить валюту: EUR')
    def setup_eur(self, request, qs):
        cntr = qs.update(cur_id='EUR')
        self.message_user(request, f'Обновлено {cntr} записей')

    @admin.action(description='Установить валюту: RUB')
    def setup_rub(self, request, qs):
        cntr = qs.update(cur_id='RUB')
        self.message_user(request, f'Обновлено {cntr} записей')

    @admin.action(description='Установить валюту: USD')
    def setup_usd(self, request, qs):
        cntr = qs.update(cur_id='USD')
        self.message_user(request, f'Обновлено {cntr} записей')


admin.site.register(Video, VideoAdmin)
admin.site.register(Director)
admin.site.register(Actor)
