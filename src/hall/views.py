from django.shortcuts import render
from rest_framework import generics
from .models import Hall
from .serializers import HallSerizlizer

# Create your views here.
class HallListApiView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerizlizer