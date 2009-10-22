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

	def __unicode__(self):
		return u'%s %s' % (self.FirstName, self.LastName)

class AttributeGroups(models.Model):
	AttributeGroupName = models.CharField(max_length = 50)
	AttributeGroupDescription = models.TextField()

	def __unicode__(self):
		return self.AttributeGroupName

class Attributes(models.Model):
	AttributeGroup = models.ForeignKey(AttributeGroups)
	AttributeValue = models.CharField(max_length = 50)

	def __unicode__(self):
		return u'%s = %s' % (self.AttributeGroup.AttributeGroupName, self.Value)

	class Meta:
		ordering = ['AttributeGroup']

class Divisions(models.Model):
	DivisionName = models.TextField()

	def __unicode__(self):
		return self.DivisionName

	class Meta:
		ordering = ['DivisionName']

class Teams(models.Model):
	TeamName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)
	Captain = models.ForeignKey(Persons, related_name = 'IntramuralsAppTeamsCaptain')
	Division = models.ForeignKey(Divisions)
	LivingUnit = models.CharField(max_length = 50)
	Members = models.ManyToManyField(Persons, related_name = 'IntramuralsAppTeamsMembers')
	
	def __unicode__(self):
		return self.TeamName

	class Meta:
		ordering = ['Division']

class Referees(models.Model):
	Person = models.ForeignKey(Persons)
	Attribute = models.ForeignKey(Attributes)
	
	def __unicode__(self):
		return u'%s %s' % (self.Person.FirstName, self.Person.LastName)

	class Meta:
		ordering = ['Person']

class Seasons(models.Model):
	SeasonStart = models.DateTimeField()
	SeasonName = models.CharField(max_length = 50)
	RegistrationStart = models.DateTimeField()
	RegistrationEnd = models.DateTimeField()
	
	def __unicode__(self):
		return self.SeasonName

	class Meta:
		ordering = ['SeasonStart']

class Leagues(models.Model):
	LeagueName = models.CharField(max_length = 50)
	Attributes = models.ManyToManyField(Attributes)
	Divisions = models.ManyToManyField(Divisions)
	Referees = models.ManyToManyField(Referees)
	
	def __unicode__(self):
		return self.LeagueName

	class Meta:
		ordering = ['LeagueName']

class Sports(models.Model):
	SportName = models.CharField(max_length = 50)
	SportRules = models.TextField()
	Leagues = models.ManyToManyField(Leagues)
	Seasons = models.ManyToManyField(Seasons)
	
	def __unicode__(self):
		return self.SportName

	class Meta:
		ordering = ['SportName']

class Locations(models.Model):
	LocationName = models.CharField(max_length = 50)
	LocationDescription = models.TextField()
	Sports = models.ManyToManyField(Sports)
	
	def __unicode__(self):
		return self.LocationName

	class Meta:
		ordering = ['LocationName']

class Games(models.Model):
	StartTime = models.DateTimeField()
	Location = models.ForeignKey(Locations)
	GameType = models.ForeignKey(Attributes, related_name = 'IntramuralsAppGamesGameType')
	HomeTeam = models.ForeignKey(Teams, related_name = 'IntramuralsAppGamesHomeTeam')
	AwayTeam = models.ForeignKey(Teams, related_name = 'IntramuralsAppGamesAwayTeam')
	HomeTeamScore = models.PositiveIntegerField()
	AwayTeamScore = models.PositiveIntegerField()
	Outcome = models.ForeignKey(Attributes, related_name = 'IntramuralsAppGamesOutcome')
	Referees = models.ManyToManyField(Referees)

	def __unicode__(self):
		return u'%s vs. %s %s' % (self.HomeTeam.TeamName, self.AwayTeam.TeamName, self.StartTime)

	class Meta:
		ordering = ['StartTime']

class Admins(models.Model):
	UserName = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.UserName

	class Meta:
		ordering = ['UserName']

