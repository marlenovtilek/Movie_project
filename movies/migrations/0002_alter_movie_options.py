# Generated by Django 4.2 on 2023-07-19 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]
