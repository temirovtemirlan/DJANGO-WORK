from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .models import Hall
from .serializers import HallSerizlizer

# Create your views here.
class HallListApiView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerizlizer


class HallCreateApiView(generics.CreateAPIView):

    serializer_class = HallSerizlizer

    def post(self, request, *args, **kwargs):
        serializer = HallSerizlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response({"message": "fail"}, status=status.HTTP_408_REQUEST_TIMEOUT)


class HallDetailViewRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerizlizer
    lookup_field = 'id'