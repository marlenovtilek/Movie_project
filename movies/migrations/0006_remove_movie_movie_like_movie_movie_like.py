# Generated by Django 4.2 on 2023-07-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_movie_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_like',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_like',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
    ]