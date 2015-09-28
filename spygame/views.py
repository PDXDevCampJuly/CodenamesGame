from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from random import choice, sample, shuffle
from .models import *
from random import randint
import string

game = Game()


def get_spy_page(request):
    if len(request.GET) != 0:
        player_type = request.GET['select']

        games = Game.objects.all()

        blue_team = games[0].team_set.create(color="blue")
        blue_team.player_set.create(type=player_type)

        red_team = games[0].team_set.create(color="red")
        red_team.player_set.create(type=player_type)

    # game_code = game.game_code_num
    # game.objects.get(game_code)
    #
    # game.team_set.
    # # spy_page = Player(type=player_type)
    # # spy_page.save()
    return render(request, 'spygamepg.html', {"player_type": player_type})

def get_spymaster_page(request):
    return render(request, 'spymastergamepg.html')

def join_or_create(request):
    """
    Home page view. A user can create a new game or join an existing one as
    the spy or spymaster client, whichever hasn't been created.
    """
    # This view is entered from a homepage post of a game code.
    if (request.method == "POST"):
        game_code = request.POST['game_code']
        print('Game code:', game_code)
        # Validate that 'game_code' is an integer
        # VALIDATION CODE GOES HERE
        games = Game.objects.all()
        # games = Game.objects.filter(password=game_code)
        # If a game hasn't been started with the entered code, redirect to
        # the homepage.
        if len(games) == 0:
            print("Games is empty.")    # Redirect to homepage
            return render('Homepg.html')
        else:
            print("Got a game to join.")
            blue_team = games[0].team_set.filter(color='blue')
            red_team = games[0].team_set.filter(color='red')
            print(games[0].team_set.filter(color='blue'))
            print(games[0].team_set.filter(color='red'))
            player_type = blue_team[0].player_set.all()[
                0].type
            # player_type = games[0].team_set.get(color='red').player_set.all()[
            #     0].type
            if player_type == 'spy':
                blue_team[0].player_set.create(type='spymaster',
                                            name='blue_master')
                red_team[0].player_set.create(type='spymaster',
                                            name='red_master')
            else:
                blue_team[0].player_set.create(type='spy',
                                            name='blue_player')
                red_team[0].player_set.create(type='spy',
                                           name='red_player')
        template = loader.get_template('spygamepg.html')
        context = RequestContext(request, {
            'display_type': player_type,
        })
        # return HttpResponse(template.render(context))
        # return render(request, 'spygamepg.html', {'display_type': player_type})
        return redirect('/spygame/get_spy_page', {'player_type': player_type})

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
