# Generated by Django 5.0.1 on 2024-02-16 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0004_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]