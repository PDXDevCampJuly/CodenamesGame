from django.shortcuts import render
from random import choice, sample, shuffle
from django.core import serializers
from .models import *
import json
from django.http import HttpResponse
from django.db.models.aggregates import Count
import random

# def Player(request):
#     data = []
#     return HttpResponse(json.dumps(data), content_type='application/json')
# Create your views here.
#data = serializers.serialize("json", Player.objects.all())

def get_spy_page(request):
    return render(request, 'spygamepg.html', {'player_type':''})

# def get_spymaster_page(request):
#     return render(request, 'spymastergamepg.html')

# def get_words(): # assign word to card
#     last = Card.objects.count() - 1
#
#     index1 = random.randint(0, last)
#
#     index2 = random.randint(0, last - 1)
#     if index2 == index1: index2 = last
#
#     MyObj1 = Card.objects.all()[index1]
#     MyObj2 = Card.objects.all()[index2]


def create_game(request):
    """
    New game is created when the spy/ spymaster page is loaded.
    """

    games = Game.objects.all()

    goFirst = choice([0, 1])


    words = list(Dictionary.objects.all())
    words = words[:25]
    # words.shuffle()

    coloredCards = []

    # Make deck of colors
    if goFirst == 1:
        # coloredCards.append('blue' * 9)
        coloredCards = ['blue' for i in range(9)]
        # coloredCards.append('red' * 8)
        coloredCards += ['red' for i in range(8)]
    else:
        coloredCards = ['blue' for i in range(8)]
        coloredCards += ['red' for i in range(9)]

    #Add colors to list

    coloredCards += ['beige' for i in range(7)]
    coloredCards += ['black']

    #Randomize color order
    # print(coloredCards)

    for i in range(len(coloredCards)):
        y_coord = i // 5
        x_coord = i % 5
        card = games[0].card_set.create(color=coloredCards.pop(), dict_word=words.pop(), y_coord=i // 5,
                                        x_coord=i % 5, revealed = False)

    return render(request, 'spygamepg.html')

from django.core import serializers

def spy_or_spymaster(request, pid):
    card = Card.objects.all()
    card_names = []
    x = 0
    while x < 25:
        y = random.choice(card)
        card_names.append(y.dict_word.word)
        x += 1
    player = Player.objects.filter(id = pid)[0]
    context = create_game(request)
    context['player_type']= player.type
    return render(request, 'spygamepg.html', {'player_type' : player.type, 'card' : json.dumps(card_names)})




# def join_or_create(request):
#      return render(request, 'Homepg.html')

    # last = Card.objects.count() - 1
    #
    # index1 = random.randint(0, last)
    #
    # index2 = random.randint(0, last - 1)
    # if index2 == index1: index2 = last
    #
    # MyObj1 = Card.objects.all()[index1]
    # MyObj2 = Card.objects.all()[index2]
    #
    # text = {
    #     'color' : MyObj1.color,
    #     'dict_word' : MyObj1.dict_word.word,
    # }
    #
    # return text



# def create_homepage_url(spy): #if button clicked, display url on homepage
#
#     if spy == True:
#         return render(request, 'spymastergamepg.html')
#     else:
#         return render(request, 'spygameph.html')


# def assign_spymaster(): # assign spymaster to team
#     pass
#
#
# def get_clue(): # allows spymaster to enter clue
#     pass
#
# def validate_clue(): # can clue be entered by spymaster
#     pass
#
# def update_cards(): # updates card with revealed attributes
#     pass
#
# def set_count(): #sets count from clue_num set by spymaster
#     pass
#
# def change_count(): # changes count of clicks players can make per turn
#     pass
#
# def switch_turn(team): # returns # of team
#     """
#     :param: team_id
#     :return: 1 or -1
#     """
#     return team * -1
#
#
# def validate_win(): #validates if player has won
#     """
#     :param:
#     :return:
#     """
#
# def pass_move(): #allows player to pass turn
#     """
#     :return: Boolean
#     """
#
#
# def remove_cards(): #replaces word on card with image
#     pass
#
# def card_click(): #allows user to click card
#     pass
#
# def prevent_click(): #prevents user from clicking board
#     pass
#
# def is_opponent(): #determines if card selected is opponent's card
#     pass
#
# def is_bystander(): #determines if card selected is bystander
#     pass
#
# def is_ally(): #determines if card selected is ally
#     pass
#
# def is_assassin(): #determines if card selected is assassin
#     pass
#
# def validate_clue_num(): #determines if spymaster clue num is valid
#     pass
#
# def main():
#     pass
