from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Dictionary)
admin.site.register(Card)
admin.site.register(Clue)