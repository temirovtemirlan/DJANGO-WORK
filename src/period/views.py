from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from src.period.models import Sessions
from src.period.serializers import SessionsSerializer


# Create your views here.
class PeriodListApiView(generics.ListAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer

class PeriodCreateApiView(generics.CreateAPIView):
    serializer_class = SessionsSerializer

    def post(self, request, *args, **kwargs):
        serializer = SessionsSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)

    # class MovieListApiView(generics.ListAPIView):
    #     queryset = Movie.objects.all()
    #     serializer_class = MovieSerializer


class PeriodDetailViewRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer
    lookup_field = 'id'