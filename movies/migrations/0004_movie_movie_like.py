# Generated by Django 4.2 on 2023-07-19 19:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_remove_movie_movie_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_like',
            field=models.ManyToManyField(default=0, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
