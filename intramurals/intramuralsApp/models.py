from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

class Person(models.Model):
	student_id = models.PositiveIntegerField()
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone_number = PhoneNumberField()
	shirt_size = models.CharField(max_length = 30)
	campus_address = models.TextField()

class Attribute(models.Model):
	name = models.TextField()
	value = models.TextField()

class League(models.Model):
	attributes = models.ManyToManyField(Attribute)

class Team(models.Model):
	team_name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 51)
	captain = models.ForeignKey(Person)
	league = models.ForeignKey(League)
	living_unit = models.CharField(max_length = 50)

