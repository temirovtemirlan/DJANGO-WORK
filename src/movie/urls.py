from django.urls import path
from .views import MovieListApiView, MovieList, MovieDetail

urlpatterns = [
    path('movie-list/', MovieListApiView.as_view()),
    path('movie-list-def/', MovieList),
    path('movie-list-def/<title>/', MovieDetail)

]