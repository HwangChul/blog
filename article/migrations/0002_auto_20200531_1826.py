# Generated by Django 3.0.5 on 2020-05-31 10:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogPost',
            new_name='ArticlePost',
        ),
    ]
