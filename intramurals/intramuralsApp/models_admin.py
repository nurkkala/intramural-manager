from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'Email',)	
	fields = ('StudentID', 'FirstName', 'LastName', 'Email', 'PhoneNumber', 'Address', 'ShirtSize',)

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

class GameAdmin(admin.ModelAdmin):
	list_display = ('StartTime', 'HomeTeam', 'AwayTeam',)
	list_filter = ('StartTime',)
	filter_horizontal = ('Referees',)
	date_hierarchy = 'StartTime'
