from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

class Person(models.Model):
	StudentID = models.PositiveIntegerField()
	FirstName = models.CharField(max_length = 30)
	LastName = models.CharField(max_length = 30)
	Email = models.EmailField()
	PhoneNumber = PhoneNumberField()
	ShirtSize = models.CharField(max_length = 30)
	Address = models.TextField()

class Attribute(models.Model):
	Name = models.TextField()
	Value = models.TextField()

class League(models.Model):
	Attributes = models.ManyToManyField(Attribute)
	LeagueName = models.CharField(max_length = 50)

class Team(models.Model):
	Members = models.ManyToManyField(Person)
	TeamName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
	CaptainID = models.ForeignKey(Person)
	LeagueID = models.ForeignKey(League)
	LivingUnit = models.CharField(max_length = 50)

class Location(models.Model):
	LocationName = models.CharField(max_length = 50)
	LocationDescription = models.TextField();

class Game(models.Model):
	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Location)
	GameType = models.TextField()
	HomeTeamID = models.ForeignKey(Team)
	AwayTeamID = models.ForeignKey(Team)
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	
class Admin(models.Model):
	UserName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)

class Referee(models.Model):
	 PersonID = models.ForeignKey(Person)
	 AttributeGroupID = models.ForeignKey(AttributeGroup)
	 
