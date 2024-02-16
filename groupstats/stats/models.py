from django.db import models

class BasicModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Summoner(BasicModel):
    summoner_name = models.CharField(max_length=31)
    summoner_tag = models.CharField(max_length=6)
    flex_league = models.CharField(max_length=15, null=True, blank=True)
    flex_lps = models.IntegerField(null=True, blank=True)
    flex_wins = models.IntegerField(default=0)
    flex_losses = models.IntegerField(default=0)
    flex_games = models.IntegerField(default=0)
    flex_winrate = models.FloatField(default=0.0)
    flex_region_rank = models.BigIntegerField(default=0)

    flex_kills = models.FloatField(default=0.0)
    flex_deaths = models.FloatField(default=0.0)
    flex_assists = models.FloatField(default=0.0)

    @property
    def kda(self):
        if self.flex_deaths == 0:
            return self.flex_kills + self.flex_assists
        else:
            return (self.flex_kills + self.flex_assists) / self.flex_deaths
    
    @property
    def log_scraping_name(self):
        return f"{self.summoner_name}-{self.summoner_tag}"
    
    @property
    def complete_name(self):
        return f"{self.summoner_name}#{self.summoner_tag}"
    
    def __str__(self):
        return f"{self.summoner_name}#{self.summoner_tag}"
    
    def __repr__(self):
        return f"{self.summoner_name}#{self.summoner_tag}"
    
    class Meta:
        db_table = 'summoner'
        unique_together = ('summoner_name', 'summoner_tag')

class SummonerGroup(BasicModel):
    name = models.CharField(max_length=31)
    summoners = models.ManyToManyField(Summoner, related_name='groups', blank=True)


class Role(models.Model):
    LANES = (
        ('T', 'Top'),
        ('J', 'Jungla'),
        ('M', 'Mid'),
        ('A', 'ADC'),
        ('S', 'Support')
    )
    lane = models.CharField(max_length=1, choices=LANES)
    flex_games = models.IntegerField(default=0)
    flex_winrate = models.FloatField(default=0.0)
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE, related_name='roles')

    class Meta:
        db_table = 'role'
        unique_together = ('summoner', 'lane')


class PlayWith(BasicModel):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE, related_name='teammates')
    played_with = models.ForeignKey(Summoner, on_delete=models.CASCADE, related_name='+')
    flex_games = models.IntegerField(default=0)
    flex_winrate = models.FloatField(default=0.0)


    class Meta:
        db_table = 'playwith'
        unique_together = ('summoner', 'played_with')

#TODO IMPLEMENTAR JUGADAS CON CADA CAMPEON
# tendria campo champion y summoner
