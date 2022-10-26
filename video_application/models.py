from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from transliterate import translit
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Actor(models.Model):
    GENDERS = [
        ('M', 'Мужчина'),
        ('F', 'Женщина')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    actor_slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('actor', args=[self.actor_slug])

    def save(self, *args, **kwargs):
        full_name = self.first_name + ' ' + self.last_name
        self.actor_slug = slugify(translit(full_name, 'ru', reversed=True))
        super(Actor, self).save(*args, **kwargs)


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    direct_email = models.EmailField()
    direct_slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        full_name = self.first_name + ' ' + self.last_name
        self.direct_slug = slugify(translit(full_name, 'ru', reversed=True))
        super(Director, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('director', args=[self.direct_slug])


class Video(models.Model):
    CURRENCY = [
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], )
    year = models.IntegerField(null=True, )
    budget = models.IntegerField(validators=[MinValueValidator(1)], null=False, default=0)
    slug = models.SlugField(default='', null=False)
    cur_id = models.CharField(max_length=3, choices=CURRENCY, default='USD')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='videosd')
    actors = models.ManyToManyField(Actor, related_name='videos')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translit(self.name, 'ru', reversed=True))
    #     super(Video,self).save(*args, **kwargs)

    def get_url(self):
        return reverse('filming', args=[self.slug])

    def __str__(self):
        return f' Название ленты - {self.name}. Рейтинг - {self.rating}. Год выпуска - {self.year}. Бюджет - {self.budget}.'
