# Generated by Django 4.2.13 on 2024-06-13 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_alter_rating_stars'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]