from django.contrib import admin
from intramurals.intramuralsApp.models import *

admin.site.register(Person, PersonAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeGroup)
admin.site.register(Division)
admin.site.register(Team, TeamAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(League)
admin.site.register(Sport)
admin.site.register(Location, LocationAdmin)
admin.site.register(Game, GameAdmin)
