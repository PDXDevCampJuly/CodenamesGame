from django.shortcuts import render
from django.core import serializers
from .models import *
import string

import json
from django.http import HttpResponse

def Player(request):
    data = []
    return HttpResponse(json.dumps(data), content_type='application/json')
# Create your views here.
#data = serializers.serialize("json", Player.objects.all())

def get_spy_page(request):
    return render(request, 'spygamepg.html')

def get_spymaster_page(request):
    return render(request, 'spymastergamepg.html')

def join_or_create(request):
    return render(request, 'Homepg.html')


def create_game(request):
    """
    New game is created when the spy/ spymaster page is loaded.
    """

    game = Game()

    #Team needs to be assigned to go first

    blueTeam = Team(game_id=game, color='blue')
    redTeam = Team(game_id=game, color='red')

    goFirst = choice(0, 1)

    words = Dictionary.objects.all()
    words.shuffle()

    coloredCards = []

    # Make deck of colors
    if goFirst == 1:
        coloredCards.append('blue' * 9)
        coloredCards.append('red' * 8)
        blueGoFirst = True
    else:
        coloredCards.append('red' * 9)
        coloredCards.append('blue' * 8)
        redGoFirst = True

    #Add colors to list

    coloredCards.append('beige' * 7)
    coloredCards.append('black')

    #Randomize color order

    coloredCards = shuffle(coloredCards)

    # Build cards with random words + random colors

    for i in range(len(coloredCards)):
        coloredCards[i] == Card(color=coloredCards.pop(), game_id=game, dict_word=words.pop())

    return render(request, 'pickSpyOrSpymaster.html')

def assign_players(): # assign player to team
    pass

def assign_spymaster(): # assign spymaster to team
    pass

def get_words(): # assign word to card
    pass

def get_clue(): # allows spymaster to enter clue
    pass

def validate_clue(): # can clue be entered by spymaster
    pass

def update_cards(): # updates card with revealed attributes
    pass

def set_count(): #sets count from clue_num set by spymaster
    pass

def change_count(): # changes count of clicks players can make per turn
    pass

def validate_click(): # validates that a player click is valid
    pass

def switch_turn(): # returns # of team
    """
    :return:
    """
    pass

def validate_win(): #validates if player has won
    pass

def pass_move(): #allows player to pass turn
    pass

def remove_cards(): #replaces word on card with image
    pass

def card_click(): #allows user to click card
    pass

def prevent_click(): #prevents user from clicking board
    pass

def is_opponent(): #determines if card selected is opponent's card
    pass

def is_bystander(): #determines if card selected is bystander
    pass

def is_ally(): #determines if card selected is ally
    pass

def is_assassin(): #determines if card selected is assassin
    if color == "black":
        return True
    pass

def validate_clue_num(): #determines if spymaster clue num is valid
    pass

def main():
    pass
