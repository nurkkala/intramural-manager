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

def currentSeason(sport): # returns the season of a sport in the current school year or 'No current season' if the sport isn't being played this year
    seasonList = sport.season_set.order_by("Start")
    today = datetime.today()
    if today.month < 7:
        schoolYearStart = today.replace(year=today.year-1, month=7, day=1)
    schoolYearStart = today.replace(year=today.year, month=7, day=1)
    schoolYearEnd = schoolYearStart.replace(year=schoolYearStart.year+1)
    currentSeason = "None"
    for season in seasonList:
        if season.Start > schoolYearStart and season.Start < schoolYearEnd:
            return season      
    return "No current season"

#"dish_out_template" belongs in /intramurals/__init.py__  (or intramuals/views.py) because dish_out_template is logically independent of any specific app, since it pulls templates from any/every app. Also, that's why dish_out_templates is in the root urls.py file.
        
def schedule(request):
    return render_to_response("schedule.html", locals())

def sports(request):
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.currentSeason = currentSeason(sport)
#    sportList = sorted(sportList, key=sportList.sport.currentSeason)
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

def standingsAllSports(request, season="None"): # generate information for all active sports
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        if season == "None": # no season specified - default to current season
            sport.season = currentSeason(sport)
        else:
            sport.season = sport.season_set.get(Name__contains=season)
        if sport.season != "No current season":
            sport.active = "true"
            sport.leagueList = sport.season.league_set.all()
            for league in sport.leagueList:
                league.divisionList = league.division_set.all()
                for division in league.divisionList:
                    division.teamList = division.team_set.all()
    return render_to_response("standingsAllSports.html", locals())

def standingsOneSport(request, sportName, season="None"): # generate information for the specified sport
    sportName = sportName.capitalize()
    sportList = Sport.objects.exclude(Name=sportName)
    for s in sportList:
        s.lwr = s.Name.lower()
        if currentSeason(s) != "No current season":
            s.active = "true";
    sport = Sport.objects.get(Name=sportName)
    if season == "None": # no season specified - default to current season
        sport.season = currentSeason(sport)
    else:
        sport.season = sport.season_set.get(Name__contains=season)
    if currentSeason(sport) != "No current season":
        active = "true";
        sport.leagueList = currentSeason(sport).league_set.all()
        for league in sport.leagueList:
            league.divisionList = league.division_set.all()
            for division in league.divisionList:
                division.teamList = division.team_set.all()
    return render_to_response("standingsOneSport.html", locals())

def record(team):
    homeWins = len(Game.objects.filter(HomeTeam__id=team.id).filter(Outcome=1)) # games won as home team
    awayWins = len(Game.objects.filter(AwayTeam__id=team.id).filter(Outcome=2)) # games won as away team
    homeLosses = len(Game.objects.filter(HomeTeam__id=team.id).filter(Outcome=2)) # games lost as home team
    awayLosses = len(Game.objects.filter(AwayTeam__id=team.id).filter(Outcome=1)) # games lost as away team
    homeTies = len(Game.objects.filter(HomeTeam__id=team.id).filter(Outcome=3)) # games tied as home team
    awayTies = len(Game.objects.filter(AwayTeam__id=team.id).filter(Outcome=3)) # games tied as away team
    wins = homeWins + awayWins
    losses = homeLosses + awayLosses
    ties = homeTies + awayTies
    record = str(wins) + "-" + str(losses)
    if ties > 0:
        record = record + "-" + str(ties)
    return record

def teamHomepage(request, teamId):
    team = Team.objects.get(id=teamId)
    team.record = record(team)
    opponentList = team.Division.team_set.all()
    memberList = team.Members.all()
    for opponent in opponentList:
        opponent.record = record(opponent)
    return render_to_response("teamHomepage.html", locals())

def register(request):
    return render_to_response("register.html", locals())

def refereesAllSports(request): # generate information for all the sports
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.seasonList = sport.season_set.all()
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()
    return render_to_response("referees.html", locals())
                    
def refereesOneSport(request, sportName): # generate information for the specified sport
    sport = Sport.objects.get(Name=sportName)
    sport.seasonList = sport.season_set.all()
    for season in sport.seasonList:
        season.leagueList = season.league_set.all()
        for league in season.leagueList:
            league.refereeList = league.Referees.all()
    return render_to_response("referees.html", locals())

def about(request):
    return render_to_response("about.html", locals())

def getX(request):
    # A serializer turns database objects into a javascript dictionary
    # This uses javascript because otherwise it would involve multiple page reloads
    json_serializer = serializers.get_serializer("json")()
    gameList = Game.objects.all()
#    for game in gameList:
#        game.homeName = game.HomeTeam.Name
#        game.homeId = game.HomeTeam.id
#        game.awayName = game.AwayTeam.Name
#        game.awayId = game.AwayTeam.id
#        game.sportId = game.HomeTeam.Division.League.Season.Sport.id
#        game.sportLogo = game.HomeTeam.Division.League.Season.Sport.id
    json_serializer.serialize(gameList)
    val = json_serializer.getvalue()
    return HttpResponse(val);

def admin(request):
    return render_to_response("admin.html", locals())

def refereeSchedule(request, refId):
    referee = Referee.objects.get(id=refId)
    gameList = referee.game_set.all()
    for game in gameList:
        game.sport = teamToSport(game.HomeTeam.id)
    return render_to_response("refereeSchedule.html", locals())

def teamToSport(teamId):
    team = Team.objects.get(id=teamId)
    sport = team.Division.League.Season.Sport
    return sport
