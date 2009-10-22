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

class AttributeGroups(models.Model):
	AttributeGroupName = models.CharField(max_length = 50)
	AttributeGroupDescription = models.TextField()

class Attributes(models.Model):
	AttributeGroupID = models.ForeignKey(AttributeGroups)
	AttributeValue = models.CharField(max_length = 50)

class Divisions(models.Model):
	DivisionName = models.TextField()
	
class Teams(models.Model):
	TeamName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
	CaptainID = models.ForeignKey(Persons, related_name = 'IntramuralsAppTeamsCaptainID')
	DivisionID = models.ForeignKey(Divisions)
	LivingUnit = models.CharField(max_length = 50)
	Members = models.ManyToManyField(Persons, related_name = 'IntramuralsAppTeamsMembers')
	
class Referees(models.Model):
	PersonID = models.ForeignKey(Persons)
	AttributeGroupID = models.ForeignKey(AttributeGroups)
	
class Seasons(models.Model):
	SeasonStart = models.DateTimeField()
	SeasonName = models.CharField(max_length = 50)
	RegistrationStart = models.DateTimeField()
	RegistrationEnd = models.DateTimeField()
	
class Leagues(models.Model):
	LeagueName = models.CharField(max_length = 50)
	Attributes = models.ManyToManyField(Attributes)
	Divisions = models.ManyToManyField(Divisions)
	Referees = models.ManyToManyField(Referees)
	
class Sports(models.Model):
	SportName = models.CharField(max_length = 50)
	SportRules = models.TextField()
	Leagues = models.ManyToManyField(Leagues)
	Seasons = models.ManyToManyField(Seasons)
	
class Locations(models.Model):
	LocationName = models.CharField(max_length = 50)
	LocationDescription = models.TextField()
	Sports = models.ManyToManyField(Sports)
	
class Games(models.Model):
	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Locations)
	GameType = models.ForeignKey(Attributes)
	HomeTeamID = models.ForeignKey(Teams, related_name = 'IntramuralsAppGamesHomeTeamID')
	AwayTeamID = models.ForeignKey(Teams, related_name = 'IntramuralsAppGamesAwayTeamID')
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	Outcome = models.ForeignKey(Attributes)
	Referees = models.ManyToManyField(Referees)

class Admins(models.Model):
	UserName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
