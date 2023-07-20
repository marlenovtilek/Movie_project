# Generated by Django 4.2 on 2023-07-19 20:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_movie_movie_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_like',
            field=models.ManyToManyField(blank=True, related_name='liked_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
