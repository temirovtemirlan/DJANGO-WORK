from django.shortcuts import render
from rest_framework import generics

from src.period.models import Sessions
from src.period.serializers import SessionsSerializer


# Create your views here.
class PeriodListApiView(generics.ListAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer


    # class MovieListApiView(generics.ListAPIView):
    #     queryset = Movie.objects.all()
    #     serializer_class = MovieSerializer