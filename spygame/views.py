from django.shortcuts import render
from random import choice, sample, shuffle
from django.core import serializers
from .models import *
import json
from django.http import HttpResponse

def Player(request):
    data = []
    return HttpResponse(json.dumps(data), content_type='application/json')
# Create your views here.
#data = serializers.serialize("json", Player.objects.all())


def generate_password():
    """Produce a 6 digit random unique integer and return it."""
    while True:
        code = choice(range(100000))
        # If the generated code does not appear in the database, it can be
        # used for a new game.
        if len(Game.objects.filter(password=code)) == 0:
            return code
        # otherwise, generate another one in the next loop


def build_board(request, current_password):
    """Build the game board."""

    # Get current game
    game = Game.objects.get(password=current_password)
    # Build a list from dictionary database table
    dictionary = Dictionary.objects.all()
    # Pick 25 random words by index from dictionary
    random_words = sample(range(1, len(dictionary)), 25)
    # Randomly select blue or red team to start
    team_to_start = choice('blue', 'red')
    # Assign colors with cells



