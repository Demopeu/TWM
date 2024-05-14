# Generated by Django 4.2.8 on 2024-05-14 05:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('overview', models.TextField()),
                ('rating', models.FloatField()),
                ('country', models.TextField()),
                ('poster_image', models.URLField()),
                ('trailer_video', models.URLField()),
                ('genre', models.TextField()),
                ('watched_users', models.ManyToManyField(related_name='watched_movies', to=settings.AUTH_USER_MODEL)),
                ('wishlist_users', models.ManyToManyField(related_name='wishlist_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
