from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'movie_tag', 'movie_published', 'movie_description','top_movie', 'movie_like']

class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'movie_tag', 'movie_published', 'movie_description', 'top_movie']

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
