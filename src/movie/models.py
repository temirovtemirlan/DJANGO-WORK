from django.db import models
from django.utils.timezone import now


class Genre(models.Model):
    title = models.CharField("Название жанра", max_length=100)

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"

    def __str__(self):
        return self.title


class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField('Название', max_length=100, blank=False, null=False)
    description = models.CharField('Описание', max_length=100, blank=False, null=False)
    release_date = models.DateField('Дата выхода', blank=False, null=False) # null=False он не может быть нулевым (обязательным)
    duration_minutes = models.IntegerField("Продолжительность", blank=False, null=False)
    genre = models.ManyToManyField(Genre, 'Жанр')
    rating = models.FloatField("Рейтинг", blank=True, null=True)
    poster_url = models.ImageField("Постер", upload_to="photos/", blank=True, null=True)

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильмы"

    def __str__(self):
        return self.title
