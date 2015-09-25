from django.db import models

# Create your models here.

class Game(models.Model):
    turn_status = models.CharField(max_length=30, blank=False)
    winner = models.CharField(max_length=30, blank=False)
    password = models.IntegerField()

class Team(models.Model):
    color = models.CharField(max_length=30, blank=False)
    game_id = models.ForeignKey(Game, default='')

    def __str__(self):
        return self.color

class Player(models.Model):
    team_id = models.ForeignKey(Team)
    name = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name

class Dictionary(models.Model):
    word = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.word

class Card(models.Model):
    game_id = models.ForeignKey(Game)
    dict_word = models.ForeignKey(Dictionary)
    color = models.CharField(max_length=30, blank=False)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    revealed = models.BooleanField()

    def __str__(self):
        return self.word

class Clue(models.Model):
    word = models.CharField(max_length=30, blank=False)
    number = models.IntegerField()
    game_id = models.ForeignKey(Game)
    team_id = models.ForeignKey(Team)

    def __str__(self):
        return self.word