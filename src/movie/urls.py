from django.urls import path
from .views import MovieListApiView, MovieCreateApiView, MovieDetailViewRUD

urlpatterns = [
    path('movie-list/', MovieListApiView.as_view()),
    path('movie-create/', MovieCreateApiView.as_view()),
    path('movie-details/<int:id>/', MovieDetailViewRUD.as_view())
]