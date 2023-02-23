# Generated by Django 4.0.3 on 2022-10-25 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_game_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='reviews.publisher'),
        ),
    ]
