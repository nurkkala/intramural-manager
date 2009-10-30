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

	def __unicode__(self):
		return u'%s %s' % (self.FirstName, self.LastName)

class AttributeGroup(models.Model):
	AttributeGroupName = models.CharField(max_length = 50)
	AttributeGroupDescription = models.TextField()

	def __unicode__(self):
		return self.AttributeGroupName

class Attribute(models.Model):
	AttributeGroup = models.ForeignKey(AttributeGroup)
	AttributeValue = models.CharField(max_length = 50)

	def __unicode__(self):
		return u'%s = %s' % (self.AttributeGroup.AttributeGroupName, self.Value)

	class Meta:
		ordering = ['AttributeGroup']

class Division(models.Model):
	DivisionName = models.TextField()

	def __unicode__(self):
		return self.DivisionName

	class Meta:
		ordering = ['DivisionName']

class Team(models.Model):
	TeamName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
	Captain = models.ForeignKey(Person, related_name = 'IntramuralsAppTeamsCaptain')
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField(max_length = 50)
	Members = models.ManyToManyField(Person, related_name = 'IntramuralsAppTeamsMembers')
	
	def __unicode__(self):
		return self.TeamName
	class Meta:
		ordering = ['Division']

class Referee(models.Model):
	Person = models.ForeignKey(Person)
	Attribute = models.ForeignKey(Attribute)
	
	def __unicode__(self):
		return u'%s %s' % (self.Person.FirstName, self.Person.LastName)

	class Meta:
		ordering = ['Person']

class Season(models.Model):
	SeasonStart = models.DateTimeField()
	SeasonName = models.CharField(max_length = 50)
	RegistrationStart = models.DateTimeField()
	RegistrationEnd = models.DateTimeField()
	
	def __unicode__(self):
		return self.SeasonName

	class Meta:
		ordering = ['SeasonStart']

class Sport(models.Model):
	SportName = models.CharField(max_length = 50)
	SportRules = models.ImageField(upload_to='SportRules')
	SportLogo = models.ImageField(upload_to='SportLogos')
	#TODO: Complete discussion about what will need to store images in the database
	Season = models.ManyToManyField(Season)
	
	def __unicode__(self):
		return self.SportName

	class Meta:
		ordering = ['SportName']

# Each league is part of one sport. For example, there might be a Men's A League
#   for basketball and a separate Men's A League in the database for soccer. This
#   allows clear division of which sports different divisions, and thus teams are
#   associated with
class League(models.Model):
	LeagueName = models.CharField(max_length = 50)
	Attribute = models.ManyToManyField(Attribute)
	Division = models.ManyToManyField(Division)
	Referee = models.ManyToManyField(Referee)
	Sport = models.ForeignKey(Sport)
	
	def __unicode__(self):
		return self.LeagueName

	class Meta:
		ordering = ['Sport']

class Location(models.Model):
	LocationName = models.CharField(max_length = 50)
	LocationDescription = models.TextField()
	Sport = models.ManyToManyField(Sport)
	
	def __unicode__(self):
		return self.LocationName

	class Meta:
		ordering = ['LocationName']

class Game(models.Model):
	OUTCOME = (
		(0, 'Won'),
		(1, 'Lost'),
		(2, 'Tied'),
		(3, 'Cancelled'),
		(4, 'Postponed')
	)

	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Location)
	GameType = models.ForeignKey(Attribute, related_name = 'IntramuralsAppGamesGameType')
	HomeTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesHomeTeam')
	AwayTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesAwayTeam')
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	Outcome = models.IntegerField(choices=OUTCOME)
	Referee = models.ManyToManyField(Referee)

	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.TeamName, self.AwayTeam.TeamName, self.StartTime)

	class Meta:
		ordering = ['StartTime']

