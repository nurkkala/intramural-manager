from django.contrib import admin
from intramuralsApp.models import *

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'Email',)	
	fields = ('StudentID', 'FirstName', 'LastName', 'Email', 'PhoneNumber', 'Address', 'ShirtSize', 'Gender')

class AttributeAdmin(admin.ModelAdmin):
	list_display = ('AttributeGroup',)

class RefereeAdmin(admin.ModelAdmin):
	list_display = ('Person', 'Attribute')

class SeasonAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Start', 'Sport',)
	date_hierarchy = 'Start'

class LeagueAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Season', 'Gender',)
	list_filter = ('Gender', 'Season',)
	filter_horizontal = ('Attributes', 'Referees',)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Division', 'LivingUnit', 'Captain',)
	list_filter = ('Division', 'Name',)
	filter_horizontal = ('Members',)
	search_fields = ('Name', 'LivingUnit',)

class LocationGroupAdmin(admin.ModelAdmin):
	filter_horizontal = ('Sports',)

class LocationAdmin(admin.ModelAdmin):
	list_display = ('Name', 'LocationGroup')
	fields = ('Name', 'LocationGroup', 'Description',)
	list_filter = ('LocationGroup',)


admin.site.register(Person, PersonAdmin)
admin.site.register(TeamMember)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeGroup)
admin.site.register(Division)
admin.site.register(Team, TeamAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Sport)
admin.site.register(LocationGroup, LocationGroupAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Game, )
