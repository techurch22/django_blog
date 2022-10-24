from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from transliterate import translit

# Create your models here.

class Video(models.Model):

    CURRENCY = [
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=15000)
    slug = models.SlugField(default='', null=False)
    cur_id = models.CharField(max_length=3, choices=CURRENCY, default='USD')

    def save_slug(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Video,self).save(*args, **kwargs)

    def get_url(self):
        return reverse('filming', args=[self.slug])

    def __str__(self):
        return f' Название ленты - {self.name}. Рейтинг - {self.rating}. Год выпуска - {self.year}. Бюджет - {self.budget}.'