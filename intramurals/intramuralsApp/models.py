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
	Address = models.TextField()
	def __unicode__(self):
		return u'%s %s' % (self.FirstName, self.LastName)
	class Meta:
		ordering = ['LastName']

class AttributeGroup(models.Model):
	AttributeGroupName = models.CharField('Group Name', max_length = 50)
	AttributeGroupDescription = models.TextField('Description')
	def __unicode__(self):
		return self.AttributeGroupName

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
	SportName = models.CharField('Name', max_length = 50)
	SportRules = models.ImageField('Rules File', upload_to='SportRules', blank=True)
	SportLogo = models.ImageField('Logo File', upload_to='SportLogos', blank=True)
	#TODO: Complete discussion about what will need to store images in the database
	def __unicode__(self):
		return self.SportName
	class Meta:
		ordering = ['SportName']

class Season(models.Model):
	SeasonName = models.CharField('Season Name', max_length = 50)
	SeasonStart = models.DateTimeField('Season Start')
	RegistrationStart = models.DateTimeField('Registration Start')
	RegistrationEnd = models.DateTimeField('Registration End')
	Sport = models.ForeignKey(Sport)
	def __unicode__(self):
		return self.SeasonName
	class Meta:
		ordering = ['Sport']

class League(models.Model):
	LeagueName = models.CharField('League Name', max_length = 50)
	Attributes = models.ManyToManyField(Attribute, verbose_name='League Classification')
	Referees = models.ManyToManyField(Referee)
	Season = models.ForeignKey(Season)
	def __unicode__(self):
		return self.LeagueName
	class Meta:
		ordering = ['Season']

class Division(models.Model):
	DivisionName = models.CharField('Division Name', max_length = 50)
	League = models.ForeignKey(League)
	def __unicode__(self):
		return self.DivisionName
	class Meta:
		ordering = ['League']

class Team(models.Model):
	TeamName = models.CharField('Name', max_length = 50)
	Password = models.CharField('Access Key', max_length = 50)
	Captain = models.ForeignKey(Person, related_name = 'IntramuralsAppTeamsCaptain', verbose_name='Team Captain')
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField('Floor/Wing', max_length = 50)
	Members = models.ManyToManyField(Person, related_name = 'IntramuralsAppTeamsMembers', verbose_name='Team Members')
	def __unicode__(self):
		return self.TeamName
	class Meta:
		ordering = ['Division']

class TeamAdmin(admin.ModelAdmin):
	list_display = ('TeamName', 'Division', 'LivingUnit',)
	list_filter = ('TeamName',)

class Location(models.Model):
	LocationName = models.CharField('Location Name', max_length = 50)
	LocationDescription = models.TextField('Description')
	Sports = models.ManyToManyField(Sport)
	def __unicode__(self):
		return self.LocationName
	class Meta:
		ordering = ['LocationName']

class Game(models.Model):
	OUTCOME = (
		(0, 'Home Win'),
		(1, 'Away Win'),
		(2, 'Tied'),
		(3, 'Cancelled'),
		(4, 'Postponed')
	)

	StartTime = models.DateTimeField('Game Start Time')
	Location = models.ForeignKey(Location)
	GameType = models.ForeignKey(Attribute, related_name = 'IntramuralsAppGamesGameType', verbose_name='Game Type')
	HomeTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesHomeTeam', verbose_name='Home Team')
	AwayTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesAwayTeam', verbose_name='Away Team')
	HomeTeamScore = models.PositiveIntegerField('Home Team Score')
	AwayTeamScore = models.PositiveIntegerField('Away Team Score')
	Outcome = models.IntegerField(choices=OUTCOME)
	Referee = models.ManyToManyField(Referee, verbose_name='Referee(s)')
	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.TeamName, self.AwayTeam.TeamName, self.StartTime)
	class Meta:
		ordering = ['StartTime']

class GameAdmin(admin.ModelAdmin):
	list_display = ('StartTime',)
	list_filter = ('StartTime',)
