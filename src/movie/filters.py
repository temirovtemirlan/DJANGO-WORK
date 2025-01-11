from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name="genre__title", lookup_expr="iexact")
    rating = filters.NumberFilter(field_name='rating', lookup_expr='exact')  # Exact match for rating
    rating_gte = filters.NumberFilter(field_name="rating", lookup_expr="gte")  # Rating >=
    rating_lte = filters.NumberFilter(field_name="rating", lookup_expr="lte")  # 2 <=
    ordering = filters.OrderingFilter(
        fields=(
            ('rating', 'rating'),  # Sorting by rating
        ),
        field_labels={
            'rating': 'Рейтинг',
        }
    )

    class Meta:
        model = Movie
        fields = ['genre', 'rating', 'ordering',"rating_gte","rating_lte"]  # Removed 'min_rating' and 'max_rating'
