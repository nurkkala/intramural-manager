from django.db import models
from django.contrib import admin
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
# Each sport uses one or more locations.
# Each location is used for one or more sports.

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
	Name = models.CharField('Name', max_length = 50) # Name of AttributeGroup
	Description = models.TextField('Description') # Description of AttributeGroup
	def __unicode__(self):
		return self.Name

class Attribute(models.Model):
	AttributeGroup = models.ForeignKey(AttributeGroup, verbose_name='Group Name')
	AttributeValue = models.CharField('Value', max_length = 50)
	def __unicode__(self):
		return u'%s = %s' % (self.AttributeGroup.AttributeGroupName, self.AttributeValue)
	class Meta:
		ordering = ['AttributeGroup']

class Referee(models.Model):
	Person = models.ForeignKey(Person, verbose_name='Referee Name')
	Attribute = models.ForeignKey(Attribute, verbose_name='Classification')
	def __unicode__(self):
		return u'%s %s' % (self.Person.FirstName, self.Person.LastName)
	class Meta:
		ordering = ['Person']

class Sport(models.Model):
	Name = models.CharField('Name', max_length = 50)
	Rules = models.ImageField('Rules File', upload_to='SportRules', blank=True)
	Logo = models.ImageField('Logo File', upload_to='SportLogos', blank=True)
	#TODO: Complete discussion about what will need to store images in the database
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Season(models.Model):
	Name = models.CharField('Season Name', max_length = 50)
	Start = models.DateTimeField('Season Start')
	RegistrationStart = models.DateTimeField('Registration Start')
	RegistrationEnd = models.DateTimeField('Registration End')
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

	Name = models.CharField('Name', max_length = 50) # Name of League
	Attributes = models.ManyToManyField(Attribute, verbose_name='League Classification') # Attributes of League
	Referees = models.ManyToManyField(Referee)
	Season = models.ForeignKey(Season)
	Gender = models.IntegerField(choices=GENDER)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Season']

class Division(models.Model):
	Name = models.CharField('Name', max_length = 50) # Name of Division
	League = models.ForeignKey(League)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['League']

class Team(models.Model):
	Name = models.CharField('Name', max_length = 50) # Name of Team
	Password = models.CharField('Access Key', max_length = 50) # Team password
	Captain = models.ForeignKey(Person, related_name = 'IntramuralsAppTeamsCaptain', verbose_name='Team Captain')
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField('Floor/Wing', max_length = 50)
	Members = models.ManyToManyField(Person, related_name = 'IntramuralsAppTeamsMembers', verbose_name='Team Members')
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Division']

class TeamAdmin(admin.ModelAdmin):
	list_display = ('TeamName', 'Division', 'LivingUnit',)
	list_filter = ('TeamName',)

class Location(models.Model):
<<<<<<< local
	LocationName = models.CharField('Location Name', max_length = 50)
	LocationDescription = models.TextField('Description')
=======
	Name = models.CharField(max_length = 50) # Name of Location
	Description = models.TextField() # Description of Location
>>>>>>> other
	Sports = models.ManyToManyField(Sport)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Game(models.Model):
	OUTCOME = (
		(0, 'Unplayed'),
		(1, 'Home Win'),
		(2, 'Away Win'),
		(3, 'Tie'),
		(4, 'Cancelled'),
		(5, 'Postponed')
	)

	GAMETYPE = (
		(0, 'Regular'),
		(1, 'Playoff'),
		(2, 'Championship')
	)
	StartTime = models.DateTimeField('Game Start Time')
	Location = models.ForeignKey(Location)
<<<<<<< local
	GameType = models.IntegerField(choices=GAMETYPE, verbose_name='Game Type')
	HomeTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesHomeTeam', verbose_name='Home Team')
	AwayTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesAwayTeam', verbose_name='Away Team')
	HomeTeamScore = models.PositiveIntegerField('Home Team Score')
	AwayTeamScore = models.PositiveIntegerField('Away Team Score')
	Outcome = models.IntegerField(choices=OUTCOME)
	Referees = models.ManyToManyField(Referee, verbose_name='Referee(s)')
	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.TeamName, self.AwayTeam.TeamName, self.Location)
	class Meta:
		ordering = ['StartTime']

class GameAdmin(admin.ModelAdmin):
	list_display = ('StartTime',)
	list_filter = ('StartTime',)
