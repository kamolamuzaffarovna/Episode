# Generated by Django 5.0.1 on 2024-02-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0003_rename_tag_episode_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=221, null=True),
        ),
    ]
