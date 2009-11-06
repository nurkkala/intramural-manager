from django import forms
from models import *

class CreateTeamForm(forms.Form):
   # floors = Location.objects.all()
   # nameList = list()
   # for floor in floors:
   #     nameList += floor.LocationName

    
    teamName = forms.CharField(max_length=100, label='Please enter the Team Name: ', required = True)
   #location = forms.ChoiceField(floors, label='Please select your location on campus: ', required = True)
    captainFirstName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s First Name: ', required = True)
    captainLastName = forms.CharField(max_length=50, label = 'Please enter the team Captain\'s Last Name: ', required = True)
    captainId = forms.IntegerField(label='Please enter the team Captain\'s school ID: ', required = True)
    captainEmail = forms.EmailField(label='Please enter the Captain\'s email address: ', required = True)
    legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
    teamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Please enter a key that your teammates will use to join the team: ', required = True)
    repeatTeamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label = 'Please enter a key that your teammates will use to join the team: ', required = True)
    

