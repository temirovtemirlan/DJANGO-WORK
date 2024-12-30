from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class MovieListApiView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET'])
def MovieList(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def MovieDetail(request, title):
    movie = Movie.objects.filter(title=title).first()
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
