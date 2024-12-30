from django.urls import path

from src.period.views import PeriodListApiView

# from .views import

urlpatterns = [
    path('sessions-list/', PeriodListApiView.as_view())
]