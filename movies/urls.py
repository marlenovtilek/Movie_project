from rest_framework import routers
from movies import views
from movies.models import Movie



movies_router = routers.DefaultRouter()
movies_router.register(r'movies_list', views.MovieViewSet, basename=Movie.__name__),
router = routers.DefaultRouter()

