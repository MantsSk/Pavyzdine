# Generated by Django 4.0.3 on 2022-10-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_game_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.IntegerField(help_text='Žaidimo įertinimas', null=True, verbose_name='rRating'),
        ),
    ]
