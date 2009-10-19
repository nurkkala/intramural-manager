from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

class Person(models.Model):
	student_id = models.PositiveIntegerField()
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone_number = PhoneNumberField()
	shirt_size = models.CharField(max_length = 30)
	campus_address = models.TextField()

class Attribute(models.Model):
	name = models.TextField()
	value = models.TextField()

class League(models.Model):
	attributes = models.ManyToManyField(Attribute)
	league_name = models.CharField(max_length = 50)

class Team(models.Model):
	members = models.ManyToManyField(Person)
	team_name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	captain = models.ForeignKey(Person)
	league = models.ForeignKey(League)
	living_unit = models.CharField(max_length = 50)

class Location(models.Model):
	location_name = models.CharField(max_length = 50)
	location_description = models.TextField();

class Game(models.Model):
	start_time = models.DateTimeField()
	location = models.ForeignKey(Location)
	game_type = models.TextField()
	home_team = models.ForeignKey(Team)
	away_team = models.ForeignKey(Team)
	home_team_score = models.PositiveIntegerField()
	away_team_score = models.PositiveIntegerField()
	
