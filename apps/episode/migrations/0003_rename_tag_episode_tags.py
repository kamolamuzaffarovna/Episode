# Generated by Django 5.0.1 on 2024-02-11 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0002_alter_comment_author_alter_comment_parent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='tag',
            new_name='tags',
        ),
    ]
