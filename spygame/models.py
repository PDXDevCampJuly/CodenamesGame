from django.db import models

# Create your models here.
class Player(models.Model):
    team_id = models.ForeignKey(Team)
    name = models.CharField(max_length=30, blank=True, null=False)
    type = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return self.name

class Team(models.Model):
    color = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return self.color

class Card(models.Model):
    game_id = models.ForeignKey(Game)
    dict_word = models.ForeignKey(Dictionary)
    color = models.CharField(max_length=30, blank=True, null=False)
    x_coord = models.IntegerField(max_length=25, blank=True, null=False)
    y_coord = models.IntegerField(max_length=25, blank=True, null=False)
    revealed = models.BooleanField()

    def __str__(self):
        return self.word

class Dictionary(models.Model):
    word = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return self.word

class Clue(models.Model):
    word = models.CharField(max_length=30, blank=True, null=False)
    number = models.IntegerField(max_length=25, blank=True, null=False)
    game_id = models.ForeignKey(Game)
    team_id = models.ForeignKey(Team)

    def __str__(self):
        return self.word

class Game(models.Model):
    turn_status = models.CharField()
    blueteam_id = models.ForeignKey(Team)
    redteam_id = models.ForeignKey(Team)
    winner = models.CharField(max_length=30, blank=True, null=False)
    password = models.IntegerField(max_length=30, blank=True, null=False)

