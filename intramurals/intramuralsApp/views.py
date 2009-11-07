# Create your views here.
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from models import *

def index(request):
    return render_to_response("home.html")

def say_hi(request, name):
    t = Template("<html><body>Well hi there {{ name_of_person }}!</body></html>")
    c = Context({'name_of_person': name})
    html = t.render(c)
    return HttpResponse(html)

def dish_out_template(request, file_name):
    return render_to_response(file_name)

def schedule(request):
    return render_to_response("schedule.html", locals())

def sports(request):
    sportList = Sport.objects.all()
    season = currentSeason() #This needs to be implemented!
    return render_to_response("sports.html", locals())

def registerTeam(request):
    if(request.POST):
        teamcaptain = request.POST["teamcaptain"]
        teamname = request.POST["teamname"]
       # teampassword = request.POST["teampassword"]
    
    return render_to_response("congrats.html", locals())

def standings(request):
    return render_to_response("standings.html", locals())

def register(request):
    return render_to_response("register.html", locals())

def registerTeam(request):
    if(request.POST):
        teamcaptain = request.POST["teamcaptain"]
        teamname = request.POST["teamname"]
       # teampassword = request.POST["teampassword"]
    
    return render_to_response("congrats.html", locals())

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


