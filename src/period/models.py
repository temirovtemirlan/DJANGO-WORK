from django.db import models
from ..hall.models import Hall
from ..movie.models import Movie


"""
movie (Фильм): Связь с моделью Movie — какой фильм показывают на этом сеансе.
hall (Зал): Связь с моделью Hall — в каком зале проходит сеанс.
start_time (Время начала): Дата и время начала сеанса. 15:00
end_time (Время окончания): Автоматически рассчитывается на основе времени начала и длительности фильма.
available_seats (Доступные места): Количество оставшихся свободных мест для бронирования.

"""

class Sessions(models.Model):
    movie = models.ManyToManyField(Movie, "Фильм")
    hall = models.ManyToManyField(Hall, "Зал")
    start_time = models.CharField("Время начала", max_length=50, blank=False, null=False)
    end_time = models.CharField("Время окончания ", max_length=50, blank=False, null=False)
    available_seats = models.IntegerField("Доступные места", blank=False, null=False)
    price = models.IntegerField('Цена', blank=False, null=False)

    def __str__(self):
        return f"{self.start_time} – {self.end_time}"
