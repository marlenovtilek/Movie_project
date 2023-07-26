from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions, status
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from movies.models import Movie
from movies.filters import MovieFilter
from movies.serializers import MovieSerializer, MovieUpdateSerializer, MovieCreateSerializer
from users.permissions import IsAdminOrReadOnly, IsUserOrReadOnly

# import requests
# from bs4 import BeautifulSoup
# from rest_framework import generics
# from .models import Movie
# from .serializers import MovieSerializer




# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly, IsUserOrReadOnly]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MovieFilter
    search_fields = ['movie_name', 'movie_tag', 'movie_genre']

    def get_serializer_class(self):
        if self.action == "update":
            return MovieUpdateSerializer
        elif self.action == "create":
            return MovieCreateSerializer
        else:
            return MovieSerializer
        
    @action(methods=["get"], detail=False, permission_classes=[IsAdminOrReadOnly])
    def top_movie(self, request):
        queryset = self.queryset.filter(top_movie=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['post'], permission_classes=[IsUserOrReadOnly])
    def like(self, request, pk=None):
        movie = self.get_object()
        user = request.user
        movie.movie_like.add(user)
        movie.save()
        return Response({"message": "Лайк успешно добавлен!"})

    @action(detail=True, methods=['post'], permission_classes=[IsUserOrReadOnly])
    def unlike(self, request, pk=None):
        movie = self.get_object()
        user = request.user
        if user in movie.movie_like.all():
            movie.movie_like.remove(user)
            return Response({"message": "Лайк успешно удален!"})
        return Response({"message": "Лайк не найден!"})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_to_favorites(self, request, pk=None):
        movie = self.get_object()
        user = request.user
        if user not in movie.favorites.all():
            movie.favorites.add(user)
            return Response({"message": "Фильм добавлен в избранное!"}, status=status.HTTP_200_OK)
        return Response({"message": "Фильм уже в избранном!"}, status=status.HTTP_400_BAD_REQUEST)



    


    # def fetch_movie_data(self):
    #     # Здесь вы должны написать код для парсинга данных с другого сайта
    #     # Используйте библиотеки, такие как requests и BeautifulSoup
    #     # Например:
    #     response = requests.get('https://www.example.com/movies')
    #     if response.status_code == 200:
    #         soup = BeautifulSoup(response.content, 'html.parser')
    #         # Здесь извлекайте информацию о фильмах, создавайте объекты Movie и сохраняйте их в базу данных

    # def list(self, request, *args, **kwargs):
    #     # Сначала выполните парсинг и сохранение данных в базу данных
    #     self.fetch_movie_data()
    #     # Затем верните список всех фильмов, сохраненных в базе данных
    #     return super().list(request, *args, **kwargs)