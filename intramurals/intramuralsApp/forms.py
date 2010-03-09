from datetime import datetime
from django import forms
from models import *
from django.db.models import Q

PHONE_REGEX = r'^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})|\d{4,5}$'  
"""Description: Matches US phone number format. 1 in the beginning is optional, area code is required, spaces or dashes can be used as optional divider between number groups. Also alphanumeric format is allowed after area code. Also, accepts campust phone numbers of 4 or 5 digits
   Matches: 1-(123)-123-1234 | 123 123 1234 | 1-800-ALPHNUM | 85555
   Non-Matches: 1.123.123.1234 | (123)-1234-123 | 123-1234"""


class CreateTeamForm1(forms.Form):
    leagues = League.objects.filter(Q(Season__RegistrationStart__lt=datetime.today()) & Q(Season__RegistrationEnd__gt=datetime.today()))
    leagueList = [ (l.id, l.Name) for l in leagues]
    sportList = [ (l.Season.Sport.id, l.Season.Sport.Name) for l in leagues]
    
    sportList = list(set(sportList)) #this is a hack way to remove duplicates from the sportList

    sportId = forms.ChoiceField(sportList, label='sport: ', required = True)
    leagueId = forms.ChoiceField(leagueList, label='league: ', required = True)
    teamName = forms.CharField(max_length=100, label='Team Name: ', required = True)
    locationId = forms.CharField(max_length=50, label='Location on campus: ', required = True)
    captainFirstName = forms.CharField(max_length=50, label = 'Captain\'s First Name: ', required = True)
    captainLastName = forms.CharField(max_length=50, label = 'Captain\'s Last Name: ', required = True)
    captainId = forms.IntegerField(label='Captain\'s school ID: ', required = True)
    captainEmail = forms.EmailField(label='Captain\'s email address: ', required = True)
    legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
    phoneNumber = forms.RegexField(PHONE_REGEX, label = 'Phone Number:', required=False)
    uPaySiteId = forms.HiddenInput()

class CreateTeamForm2(forms.Form):
    teamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Please enter a key that your teammates will use to join the team: ', required = True)
    repeatTeamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label = 'Please enter a key that your teammates will use to join the team: ', required = True)
    emailList = forms.CharField(label = 'Please enter a list of e-mail addresses', required=False)

class JoinTeamForm1(forms.Form):
    teamPassword = forms.CharField(max_length=50, label="Enter team password so we know which team you want to sign up for (ask your captain if you don't know it)", required=True)

class JoinTeamForm2(forms.Form):
    playerFirstName = forms.CharField(max_length=40, label = 'First name:', required=True)
    playerLastName = forms.CharField(max_length=40, label = 'Last name:', required=True)
    playerEmail = forms.EmailField(max_length=40, label = 'E-mail address:', required=True)
    shirtSize = forms.ChoiceField(list(Person.SHIRTSIZE), label = 'Select your shirt-size so you can wear a shirt when you win the championship', required=True)
    phoneNumber = forms.RegexField(PHONE_REGEX, label = 'Phone Number (only visible to your teammates):', required=False)
    
