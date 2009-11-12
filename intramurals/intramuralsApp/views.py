from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime
from models import *
from forms import *
from django.core import serializers
import json

def index(request):
    return render_to_response("home.html")

def say_hi(request, name):
    t = Template("<html><body>Well hi there {{ name_of_person }}!</body></html>")
    c = Context({'name_of_person': name})
    html = t.render(c)
    return HttpResponse(html)

def currentSeason(sport):
    seasonList = sport.season_set.order_by("Start")
    now = datetime.now()
    currentSeason = seasonList[0]
    minimum = (abs(currentSeason.Start - now)).days
    for season in seasonList:
        difference = (abs(season.Start - now)).days
        if difference < minimum:
            minimum = difference
            currentSeason = season
    return currentSeason;

#"dish_out_template" belongs in /intramurals/__init.py__  (or intramuals/views.py) because dish_out_template is logically independent of any specific app, since it pulls templates from any/every app. Also, that's why dish_out_templates is in the root urls.py file.
        
def schedule(request):
    return render_to_response("schedule.html", locals())

def sports(request):
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.currentSeason = currentSeason(sport)
    return render_to_response("sports.html", locals())

# I Need To Get The
# hard-coded copies to be
# created dynamically!!!!
def createTeam(request):
    form = CreateTeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if request.POST['teamPassword'] == request.POST["repeatTeamPassword"]:
                cd = form.cleaned_data
                league = League.objects.get(id=leagueId)
                division = league.division_set.filter(name = "Unassigned")
                captain = Person(StudentID=cd['captainId'], FirstName=cd['captainFirstName'], LastName=cd['captainLastName'], Email=cd['captainEmail'], ShirtSize="XXL", Address="236 W. Reade Ave.")
                captain.save()
                team = Team(TeamName=cd['teamName'], Password=cd['teamPassword'], Captain=captain, Division = division, LivingUnit="Sammy II")
                team.save()
                return render_to_response("congrats.html", locals())

            else: 
                return render_to_response("createTeam.html", {"pword_error":True})
        else:   
            return render_to_response("createTeam.html", locals())
    else:
        return render_to_response("createTeam.html", locals())
 
def standings(request):
    return render_to_response("standings.html", locals())

def register(request):
    return render_to_response("register.html", locals())

def referees(request):
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.seasonList = sport.season_set.all()
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()
    return render_to_response("referees.html", locals())

def about(request):
    return render_to_response("about.html", locals())

def getX(request):
    #json_serializer = serializers.get_serializer("json")()
    #json_serializer.serialize(Game.objects().all())
    return HttpResponse(json.dumps({'a':9}));

def admin(request):
    return render_to_response("admin.html", locals())

def refereeSchedule(request, refId):
    referee = Referee.objects.get(id=refId)
    gameList = referee.game_set.all()
   # for game in gameList:
   #     game.sport = teamToSport(game.HomeTeam)
    return render_to_response("refereeSchedule.html", locals())

def teamToSport(teamName):
    team = Team.objects.get(TeamName=teamName)
    sport = team.division.league.season.sport
    return sport
