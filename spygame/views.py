from django.shortcuts import render
from random import choice, sample, shuffle
from .models import *
from random import randint
import string

game = Game()


def get_spy_page(request):
    

    player_type = request.GET['select']
    spy_page = Player(type=player_type)
    spy_page.save()
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

#
def spy_or_spymaster(request):
    print(request.GET)
    create_game_code()
    return render(request, 'pickSpyOrSpymaster.html')
#
def create_game_code(): #if button clicked, display url on homepage
    new_code = randint(1000000,9999999)
    game = Game(password=new_code)
    game.save()

    #game_code_num = apps.get_model("spygame", "Game")
    #game.password = new_code
#
#def assign_player(): # assign spym


# def get_words(): # assign word to card
#     pass
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
#joi
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
>>>>>>> 5d6f8f721c03fd128061cb9e9bdbef379fb238f0
