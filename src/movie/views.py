from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .filters import MovieFilter
from .models import Movie
from .serializers import MovieSerializer


# list -> get req
# create -> post req

# Create your views here.
class MovieListApiView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter



class MovieCreateApiView(generics.CreateAPIView):

    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response({"message": "fail"}, status=status.HTTP_408_REQUEST_TIMEOUT)


class MovieDetailViewRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    # PUT,PATCH,DELETE
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id' # primary key or id

