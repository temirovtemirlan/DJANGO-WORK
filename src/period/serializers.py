from rest_framework import serializers
from .models import Sessions
from ..hall.serializers import HallSerizlizer
from ..movie.serializers import MovieSerializer


class SessionsSerializer(serializers.ModelSerializer):

    hall = HallSerizlizer(many=True)
    movie = MovieSerializer(many=True)

    class Meta:
        model = Sessions
        fields = ('hall','start_time','end_time','available_seats','price', 'movie')
