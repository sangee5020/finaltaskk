# Generated by Django 4.2.8 on 2024-03-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_rating_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
