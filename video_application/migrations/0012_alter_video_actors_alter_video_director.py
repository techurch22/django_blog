# Generated by Django 4.1.2 on 2022-10-26 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_application', '0011_actor_actor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='actors',
            field=models.ManyToManyField(related_name='videos', to='video_application.actor'),
        ),
        migrations.AlterField(
            model_name='video',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='video_application.director'),
        ),
    ]
