from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    points_per_game = models.FloatField()
    rebounds_per_game = models.FloatField()
    assists_per_game = models.FloatField()

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateField()
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"