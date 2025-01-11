from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id","title")

class MovieSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True) # может быть много значений если manyToMany то должен быть many

    class Meta:
        model = Movie
        fields = ('id','title','description',
                  'release_date','duration_minutes','genre',
                  'rating','poster_url', 'created_at', 'updated_at')