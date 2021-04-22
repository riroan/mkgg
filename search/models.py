from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)

    soloTier = models.CharField(max_length=20, default="UNRANK")
    soloLeaguePoint = models.IntegerField(default=0)
    soloWins = models.IntegerField(default=0)
    soloLosses = models.IntegerField(default=0)

    flexTier = models.CharField(max_length=20, default="UNRANK")
    flexLeaguePoint = models.IntegerField(default=0)
    flexWins = models.IntegerField(default=0)
    flexLosses = models.IntegerField(default=0)

    updateDate = models.DateTimeField()
    summonerLevel = models.IntegerField()
    profileIconId = models.IntegerField()

    def __str__(self):
        return self.userName


class Match(models.Model):
    gameId = models.IntegerField(primary_key=True)
    platformId = models.CharField(max_length=5, default="KR")
    gameDuration = models.IntegerField(default=0)
    queueId = models.IntegerField(default=0)
    mapId = models.IntegerField(default=0)
    seasonId = models.IntegerField(default=0)
    gameMode = models.CharField(max_length=10, default="CLASSIC")
    gameType = models.CharField(max_length=20, default="MATCHED_GAME")


class Participants(models.Model):
    gameId = models.ForeignKey(Match, on_delete=models.CASCADE)
    participantId = models.IntegerField(default=1)
    teamId = models.IntegerField(default=100)
    championId = models.IntegerField(default=0)
    spell1Id = models.IntegerField(default=0)
    spell2Id = models.IntegerField(default=0)
    win = models.BooleanField(default=False)

    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)
    item4 = models.IntegerField(default=0)
    item5 = models.IntegerField(default=0)
    item6 = models.IntegerField(default=0)

    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    largestKillingSpree = models.IntegerField(default=0)
    largestMultiKill = models.IntegerField(default=0)

    longestTimeSpentLiving = models.IntegerField(default=0)
    doubleKills = models.IntegerField(default=0)
    tripleKills = models.IntegerField(default=0)
    quadraKills = models.IntegerField(default=0)
    pentaKills = models.IntegerField(default=0)

    totalDamageDealt = models.IntegerField(default=0)

    visionScore = models.IntegerField(default=0)
    champLevel = models.IntegerField(default=0)

    lane = models.CharField(max_length=10, default="TOP")


class UserMatch(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    platformId = models.CharField(max_length=5, default="KR")
    gameId = models.IntegerField(default=0)
    champion = models.IntegerField(default=0)
    season = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=0)
    role = models.CharField(max_length=10, default="NONE")
    lane = models.ForeignKey(Participants, on_delete=models.CASCADE)
