# Generated by Django 4.1.7 on 2024-03-18 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240214_2331'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Planning',
        ),
        migrations.DeleteModel(
            name='RevokedToken',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]