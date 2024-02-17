# Generated by Django 5.0.1 on 2024-02-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0007_episodefilter_episode_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='filter',
            field=models.ManyToManyField(limit_choices_to=models.Q(('filter', '*'), _negated=True), to='episode.episodefilter'),
        ),
    ]