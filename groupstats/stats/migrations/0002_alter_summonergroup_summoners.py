# Generated by Django 4.1.13 on 2024-02-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summonergroup',
            name='summoners',
            field=models.ManyToManyField(blank=True, related_name='groups', to='stats.summoner'),
        ),
    ]
