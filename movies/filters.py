from django_filters import rest_framework as rest_filters, CharFilter

from movies.models import Movie

class MovieFilter(rest_filters.FilterSet):
    movie_genre = CharFilter(field_name='movie_genre', lookup_expr='icontains')
    movie_tag = CharFilter(field_name='movie_tag', lookup_expr='icontains')
    movie_published = CharFilter(field_name='movie_published', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['movie_genre', 'movie_tag', 'movie_published']