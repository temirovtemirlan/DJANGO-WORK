from django.urls import path

from src.period.views import PeriodListApiView, PeriodCreateApiView, PeriodDetailViewRUD

# from .views import

urlpatterns = [
    path('period-list/', PeriodListApiView.as_view()),
    path('period-create/', PeriodCreateApiView.as_view()),
    path('period-details/<int:id>', PeriodDetailViewRUD.as_view())
]