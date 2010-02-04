from datetime import datetime
from django import forms
from models import *

class CreateTeamForm1(forms.Form):
    today = datetime.today()
    intYear = today.year
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=yearStart.year+1)

    sportListA = Sport.objects.filter(season__RegistrationStart__range=(yearStart, today)).distinct()
    sportListB = sportListA.filter(season__RegistrationEnd__range=(today, yearEnd)).distinct()

    sportList = [(obj.id, obj.Name) for obj in sportListB]
    leagueList = [(obj.id, obj.Name) for obj in League.objects.all()]
    
    sportId = forms.ChoiceField(sportList, label='Please select the sport: ', required = True)
    leagueId = forms.ChoiceField(leagueList, label='Please select the league: ', required = True)
    teamName = forms.CharField(max_length=100, label='Please enter the Team Name: ', required = True)
    locationId = forms.CharField(max_length=50, label='Please select your location on campus: ', required = True)
    captainFirstName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s First Name: ', required = True)
    captainLastName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s Last Name: ', required = True)
    captainId = forms.IntegerField(label='Please enter the team Captain\'s school ID: ', required = True)
    captainEmail = forms.EmailField(label='Please enter the Captain\'s email address: ', required = True)
    legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
    uPaySiteId = forms.HiddenInput()

class CreateTeamForm2(forms.Form):
    teamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Please enter a key that your teammates will use to join the team: ', required = True)
    repeatTeamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label = 'Please enter a key that your teammates will use to join the team: ', required = True)
    emailList = forms.CharField(label = 'Please enter a list of e-mail addresses', required=False)

class JoinTeamForm1(forms.Form):
    teamPassword = forms.CharField(max_length=50, label="Please Enter team password so we know which team you want to sign up for", required=True)
