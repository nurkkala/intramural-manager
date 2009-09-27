from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

# Create your models here.

class Person(models.Model):
	student_id = models.PositiveIntegerField()
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone_number = PhoneNumberField()
	shirt_size = models.CharField(max_length = 30)
	campus_address = models.TextField()

class Sport(models.Model):
	sport_name = models.CharField(max_length = 50)
	rules = models.TextField()

class League(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('B', 'Co-ed'),
	)
	league_name = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
	sport = models.ForeignKey(Sport)

class Team(models.Model):
	team_name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 51)
	captain = models.ForeignKey(Person)
	league = models.ForeignKey(League)
	living_unit = models.CharField(max_length = 50)
		
class StartEndTime(models.Model):
	StartTime = models.DateTimeField()
	EndTime = models.DateTimeField()

	
