from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

# Each person is part of one or more teams and/or is a referee.
# Each team has one or more team members (people) and one captain (person)
# Each referee is part of one or more leagues.
# Each league has one or more referees (people).
# Each referee is assigned to one or more games.
# Each game is assigned one or more referees.
# Each team is part of one division.
# Each division has one or more teams.
# Each division is part of one league.
# Each league has one or more divisions.
# Each league is part of one season.
# Each season has one or more leagues.
# Each season is part of one sport.
# Each sport has one or more seasons.
# Each location is part of one location group.
# Each location group has one or more locations
# Each location group is used for one or more sports.
# Each sport uses one or more locations.

class Person(models.Model):
	StudentID = models.PositiveIntegerField()
	FirstName = models.CharField(max_length = 50)
	LastName = models.CharField(max_length = 50)
	Email = models.EmailField()
	PhoneNumber = PhoneNumberField(null=True)
	ShirtSize = models.CharField(max_length = 50)
	Address = models.CharField(max_length = 50)
	def __unicode__(self):
		return u'%s %s' % (self.FirstName, self.LastName)
	class Meta:
		ordering = ['LastName']

class AttributeGroup(models.Model):
	Name = models.CharField(max_length = 50) # Name of AttributeGroup
	Description = models.TextField() # Description of AttributeGroup
	def __unicode__(self):
		return self.Name

class Attribute(models.Model):
	AttributeGroup = models.ForeignKey(AttributeGroup)
	AttributeValue = models.CharField(max_length = 50)
	def __unicode__(self):
		return u'%s = %s' % (self.AttributeGroup.AttributeGroupName, self.Value)
	class Meta:
		ordering = ['AttributeGroup']

class Referee(models.Model):
	Person = models.ForeignKey(Person)
	Attribute = models.ForeignKey(Attribute)
	def __unicode__(self):
		return u'%s %s' % (self.Person.FirstName, self.Person.LastName)
	class Meta:
		ordering = ['Person']

class Sport(models.Model):
	Name = models.CharField(max_length = 50) # Name of Sport
	Rules = models.ImageField(upload_to='SportRules') # Rules for Sport
	Logo = models.ImageField(upload_to='SportLogos') # Logo for Sport
	Photo = models.ImageField(upload_to='SportPhotos') # Photo for Sport
	#TODO: Complete discussion about what we will need to store images in the database
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Season(models.Model):
	Name = models.CharField(max_length = 50) # Name of Season
	Start = models.DateTimeField() # Start time of Season
	RegistrationStart = models.DateTimeField()
	RegistrationEnd = models.DateTimeField()
	Sport = models.ForeignKey(Sport)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Sport']

class League(models.Model):
	GENDER = (
		(0, 'Male'),
		(1, 'Female'),
		(2, 'Coed')
	)

	Name = models.CharField(max_length = 50) # Name of League
	Attributes = models.ManyToManyField(Attribute) # Attributes of League
	Referees = models.ManyToManyField(Referee)
	Season = models.ForeignKey(Season)
	Gender = models.IntegerField(choices=GENDER)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Season']

class Division(models.Model):
	Name = models.CharField(max_length = 50) # Name of Division
	League = models.ForeignKey(League)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['League']

class Team(models.Model):
	Name = models.CharField(max_length = 50) # Name of Team
	Password = models.CharField(max_length = 50) # Team password
	Captain = models.ForeignKey(Person, related_name = 'IntramuralsAppTeamsCaptain')
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField(max_length = 50)
	Members = models.ManyToManyField(Person, related_name = 'IntramuralsAppTeamsMembers')
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Division']

class LocationGroup(models.Model):
	Name = models.CharField(max_length = 50)
	Sports = models.ManyToManyField(Sport)
	Map = models.ImageField(upload_to='LocationMaps')
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Location(models.Model):
	Name = models.CharField(max_length = 50) # Name of Location
	Description = models.TextField() # Description of Location
	LocationGroup = models.ForeignKey(LocationGroup)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Game(models.Model):
	OUTCOME = (
		(0, 'Unplayed'),
		(1, 'Won'),
		(2, 'Lost'),
		(3, 'Tied'),
		(4, 'Cancelled'),
		(5, 'Postponed')
	)

	GAMETYPE = (
		(0, 'Regular'),
		(1, 'Playoff'),
		(2, 'Championship')
	)
	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Location)
	GameType = models.IntegerField(choices=GAMETYPE)
	HomeTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesHomeTeam')
	AwayTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesAwayTeam')
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	Outcome = models.IntegerField(choices=OUTCOME)
	Referees = models.ManyToManyField(Referee)
	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.TeamName, self.AwayTeam.TeamName, self.Location)
	class Meta:
		ordering = ['StartTime']

