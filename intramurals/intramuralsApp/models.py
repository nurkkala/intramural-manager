from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

class Persons(models.Model):
	StudentID = models.PositiveIntegerField()
	FirstName = models.CharField(max_length = 30)
	LastName = models.CharField(max_length = 30)
	Email = models.EmailField()
	PhoneNumber = PhoneNumberField()
	ShirtSize = models.CharField(max_length = 30)
	Address = models.TextField()

class Sport(models.Model):
	SportName = models.CharField(max_length = 50)
	Rules = models.TextField()

class Attributes(models.Model):
	Name = models.TextField()
	Value = models.TextField()

class Leagues(models.Model):
	Attributes = models.ManyToManyField(Attribute)
	LeagueName = models.CharField(max_length = 50)

class Teams(models.Model):
	Members = models.ManyToManyField(Person)
	TeamName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
	CaptainID = models.ForeignKey(Person)
	LeagueID = models.ForeignKey(League)
	LivingUnit = models.CharField(max_length = 50)

class Locations(models.Model):
	LocationName = models.CharField(max_length = 50)
	LocationDescription = models.TextField();

class Games(models.Model):
	Referees = models.ManyToMany(Referee)
	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Location)
	GameType = models.TextField()
	HomeTeamID = models.ForeignKey(Team)
	AwayTeamID = models.ForeignKey(Team)
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	
class Admins(models.Model):
	UserName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)

class Referees(models.Model):
	PersonID = models.ForeignKey(Person)
	AttributeGroupID = models.ForeignKey(AttributeGroup)
	
class Divisions(models.Model):
	DivisionName = models.TestField()

class Seasons(models.Model):
	SeasonStart = models.DateTimeField()
	SeasonName = models.CharField(max_length = 50)
	RegistrationStart = models.DateTimeField()
	RegistrationEnd = models.DateTimeField()
