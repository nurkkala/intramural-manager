from django.db import models
from django.contrib import admin
from django.contrib.localflavor.us.models import PhoneNumberField
from sandbox import *

class Person(models.Model):
	SHIRTSIZE = (
		('XS', 'XS'),
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
		('XXL', 'XXL'),
		('XXXL', 'XXXL')
	)
	GENDER = (
		(0, 'Male'),
		(1, 'Female'),
	)

	Gender = models.IntegerField(choices=GENDER)
	StudentID = models.PositiveIntegerField('Student ID')
	FirstName = models.CharField('First Name', max_length = 50)
	LastName = models.CharField('Last Name', max_length = 50)
	Email = models.EmailField()
	PhoneNumber = PhoneNumberField('Phone Number', null=True)
	ShirtSize = models.CharField('Shirt Size', choices=SHIRTSIZE, max_length = 5)
	Address = models.CharField('Address', max_length = 50)
	def __unicode__(self):
		return u'%s %s' % (self.FirstName, self.LastName)
	def name(obj):
		return ("%s %s" % (obj.FirstName, obj.LastName))
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
		return u'%s = %s' % (self.AttributeGroup, self.AttributeValue)
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
	Name = models.CharField('Name', max_length = 50, unique=True)
	#Rules = models.ImageField('Rules File', upload_to='SportRules', blank=True)
	#Logo = models.ImageField('Logo File', upload_to='SportLogos', blank=True)
	#Photo = models.ImageField('Sport Photo', upload_to='SportPhotos', blank=True) # Photo for Sport
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
	Referees = models.ManyToManyField(Referee, verbose_name='Referee(s)')
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
	Captain = models.ForeignKey(Person, related_name = 'IntramuralsAppTeamsCaptain', verbose_name='Team Captain', blank=True, null=True)
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField('Floor/Wing', max_length = 50)
	Members = models.ManyToManyField(Person, through = 'TeamMember')

	def __unicode__(self):
		return (self.Name)
		#return '<a href="%s/team/%d">%s</a>' % (URL_PREFIX, self.id , self.Name)
	class Meta:
		ordering = ['Division']
		unique_together=(("Name","Division"),("Password","Division"))

class TeamRanking(models.Model):
	Team = models.ForeignKey(Team, primary_key=True)
	wins = models.IntegerField()
	losses = models.IntegerField()
	ties = models.IntegerField()
	rank = models.FloatField()
	class Meta:
		managed = False
		
class TeamMember(models.Model):
	PAYMENTSTATUS = (
			(0, 'Payment Pending'),
			(1, 'Paid')
	)

	Member = models.ForeignKey(Person)
	Team = models.ForeignKey(Team)
	PaymentStatus = models.IntegerField(choices=PAYMENTSTATUS, default=0)
	def __unicode__(self):
		return u'%s :: %s is on team %s' % (self.PaymentStatus, self.Member, self.Team)

class LocationGroup(models.Model):
	Name = models.CharField('Location Name', max_length = 50)
	Sports = models.ManyToManyField(Sport, verbose_name='Sports Played')
	#Map = models.ImageField('Location Map', upload_to='LocationMaps', blank=True)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Location(models.Model):
	Name = models.CharField('Name', max_length = 50)
	Description = models.TextField('Description')
	LocationGroup = models.ForeignKey(LocationGroup, verbose_name='Location')
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Game(models.Model):
	OUTCOME = (
		(0, 'Unplayed'),
		(1, 'Home Win'), #TODO: delete home/away/tie  rename here and below to "status"
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
	GameType = models.IntegerField(choices=GAMETYPE, verbose_name='Game Type')
	HomeTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesHomeTeam', verbose_name='Home Team')
	AwayTeam = models.ForeignKey(Team, related_name = 'IntramuralsAppGamesAwayTeam', verbose_name='Away Team')
	HomeTeamScore = models.PositiveIntegerField('Home Team Score') #TODO: default = null
	AwayTeamScore = models.PositiveIntegerField('Away Team Score')
	Outcome = models.IntegerField(choices=OUTCOME)
	Referees = models.ManyToManyField(Referee, verbose_name='Referee(s)')
	League = models.ForeignKey(League)
	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.Name, self.AwayTeam.Name, self.Location)
	class Meta:
		ordering = ['StartTime']

class CurrentLeagues(models.Model):
	League = models.ForeignKey(League, primary_key=True)
	class Meta:
		managed = False

class OpenTeam(models.Model):
	Name = models.CharField('Name', max_length = 50) # Name of Team
	Password = models.CharField('Access Key', max_length = 50) # Team password
	Captain = models.ForeignKey(Person, verbose_name='Team Captain', related_name="Captain")
	Division = models.ForeignKey(Division)
	LivingUnit = models.CharField('Floor/Wing', max_length = 50)
#	Members = models.ManyToManyField(Person, through = 'TeamMember', related_name="Members")

	class Meta:
		managed = False
	def __unicode__(self):
		return u'%s' % (self.Name)

class OpenLeague(models.Model):
	GENDER = (
		(0, 'Male'),
		(1, 'Female'),
		(2, 'Coed')
	)

	Name = models.CharField('Name', max_length = 50) # Name of League
	Attributes = models.ManyToManyField(Attribute, verbose_name='League Classification') # Attributes of League
	Referees = models.ManyToManyField(Referee, verbose_name='Referee(s)')
	Season = models.ForeignKey(Season)
	Gender = models.IntegerField(choices=GENDER)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Season']
		managed = False

