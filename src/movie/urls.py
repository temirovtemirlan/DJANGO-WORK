from django.urls import path
from .views import MovieListApiView

urlpatterns = [
    path('movie-list/', MovieListApiView.as_view())
]