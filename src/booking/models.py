from django.db import models

from src.custom_user.models import CustomUser
from src.period.models import Sessions

# Create your models here.
class Booking(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ("Наличными","Наличными"),
        ("Карта", "Карта"),
    ]

    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", related_name="user", on_delete=models.CASCADE)
    count_place = models.IntegerField(verbose_name="Количество мест", blank=False, null=False)
    period = models.ForeignKey( Sessions, verbose_name="Период", related_name="period", on_delete=models.CASCADE)
    payment_type = models.CharField(verbose_name="Тип оплаты", choices=PAYMENT_TYPE_CHOICES)
    price = models.IntegerField(verbose_name="Цена билета", blank=True, null=True, default='sdf')
    bonus = models.IntegerField(verbose_name="Твои бонусы", blank=True, null=True)

    class Meta:
        verbose_name = "Бронирования"
        verbose_name_plural = "Бронирование"

    def __str__(self):
        return f"{self.user} Оплата: {self.payment_type}"

    def save(self, *args, **kwargs):
        # Убедимся, что bonus имеет значение по умолчанию, если оно None
        if self.bonus is None:
            self.bonus = 0

        self.user.wallet += self.bonus
        super(Booking, self).save(*args, **kwargs)