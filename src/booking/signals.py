from django.db.models.signals import post_save
from django.dispatch import receiver
from src.booking.models import Booking

@receiver(post_save, sender=Booking)
def save_booking(sender, instance, created, **kwargs):
    if not created:
        # Сигнал срабатывает только для нового бронирования
        return

    hall = instance.period.hall
    seats_counter = hall.seats
    booking_counter = instance.count_place

    if booking_counter <= seats_counter:
        # Обновляем количество мест в зале
        hall.seats -= booking_counter
        hall.save()
    else:
        raise ValueError("Количество мест для бронирования превышает доступное.")
