from django.urls import path
from .views import HallListApiView

urlpatterns = [
    path('hall-list/', HallListApiView.as_view())
]