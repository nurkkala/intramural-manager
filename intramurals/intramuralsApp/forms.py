from django import forms
from models import *

class CreateTeamForm(forms.Form):
    sportList = [(obj.id, obj.Name) for obj in Sport.objects.all()]
    leagueList = [(obj.id, obj.Name) for obj in League.objects.all()]
    locationList = [(obj.id, obj.Name) for obj in Location.objects.all()]
    
    sportId = forms.ChoiceField(sportList, label='Please select the sport: ', required = True)
    leagueId = forms.ChoiceField(leagueList, label='Please select the league: ', required = True)
    teamName = forms.CharField(max_length=100, label='Please enter the Team Name: ', required = True)
    locationId = forms.ChoiceField(locationList, label='Please select your location on campus: ', required = True)
    captainFirstName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s First Name: ', required = True)
    captainLastName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s Last Name: ', required = True)
    captainId = forms.IntegerField(label='Please enter the team Captain\'s school ID: ', required = True)
    captainEmail = forms.EmailField(label='Please enter the Captain\'s email address: ', required = True)
    legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
    teamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Please enter a key that your teammates will use to join the team: ', required = True)
    repeatTeamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label = 'Please enter a key that your teammates will use to join the team: ', required = True)
    
