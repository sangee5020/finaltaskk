# Generated by Django 4.2.8 on 2024-03-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
