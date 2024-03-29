# Generated by Django 4.1.13 on 2024-02-16 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summoner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('summoner_name', models.CharField(max_length=31)),
                ('summoner_tag', models.CharField(max_length=6)),
                ('flex_league', models.CharField(blank=True, max_length=15, null=True)),
                ('flex_lps', models.IntegerField(blank=True, null=True)),
                ('flex_wins', models.IntegerField(default=0)),
                ('flex_losses', models.IntegerField(default=0)),
                ('flex_games', models.IntegerField(default=0)),
                ('flex_winrate', models.FloatField(default=0.0)),
                ('flex_region_rank', models.BigIntegerField(default=0)),
                ('flex_kills', models.FloatField(default=0.0)),
                ('flex_deaths', models.FloatField(default=0.0)),
                ('flex_assists', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'summoner',
                'unique_together': {('summoner_name', 'summoner_tag')},
            },
        ),
        migrations.CreateModel(
            name='SummonerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=31)),
                ('summoners', models.ManyToManyField(blank=True, null=True, related_name='groups', to='stats.summoner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane', models.CharField(choices=[('T', 'Top'), ('J', 'Jungla'), ('M', 'Mid'), ('A', 'ADC'), ('S', 'Support')], max_length=1)),
                ('flex_games', models.IntegerField(default=0)),
                ('flex_winrate', models.FloatField(default=0.0)),
                ('summoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='stats.summoner')),
            ],
            options={
                'db_table': 'role',
                'unique_together': {('summoner', 'lane')},
            },
        ),
        migrations.CreateModel(
            name='PlayWith',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flex_games', models.IntegerField(default=0)),
                ('flex_winrate', models.FloatField(default=0.0)),
                ('played_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stats.summoner')),
                ('summoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teammates', to='stats.summoner')),
            ],
            options={
                'db_table': 'playwith',
                'unique_together': {('summoner', 'played_with')},
            },
        ),
    ]
