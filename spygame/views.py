from django.shortcuts import render

from django.core import serializers
from .models import *
import json
from django.http import HttpResponse

def Player(request):
    data = []
    return HttpResponse(json.dumps(data), content_type='application/json')
# Create your views here.
#data = serializers.serialize("json", Player.objects.all())