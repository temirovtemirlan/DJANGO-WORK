from django.db import models

"""
name (Название зала): Уникальное название или номер зала (например, "Зал 1").
seats (Количество мест): Общее количество мест в зале.
description (Описание): Дополнительная информация (например, "VIP-зал с кожаными креслами").
available_equipment (Оборудование): Информация об оборудовании (например, "3D, Dolby Atmos").

"""


class Hall(models.Model):
    name = models.CharField("Название зала", max_length=100, blank=False,null=False)
    seats = models.IntegerField("Количество мест", blank=False, null=False)
    description = models.CharField("Описание", max_length=500, blank=False,null=False)
    available_equipment = models.CharField("Оборудование", max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "зал"
        verbose_name_plural = "залы"

    def __str__(self):
        return self.name