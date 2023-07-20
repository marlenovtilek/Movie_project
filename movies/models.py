from django.db import models
from django.core.validators import MaxValueValidator
from users.models import User

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField("Название фильма", max_length=100, null=True)
    movie_image = models.ImageField("Картинка фильма", upload_to="movie_images", null=True)
    movie_genre = models.CharField("Жанр фильма", max_length=100, null=True)
    movie_tag = models.TextField("Теги фильма", null=True)
    movie_published = models.IntegerField("Год выпуска", null=True, validators=[MaxValueValidator(2050)])
    movie_description = models.TextField("Описание фильма")
    top_movie = models.BooleanField(default=False)
    movie_like = models.PositiveIntegerField('Лайки', default=0)


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.movie_name