rfrom django.http import HttpResponse
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


#"dish_out_template" belongs in /intramurals/__init.py__  (or intramuals/views.py) because dish_out_template is logically independent of any specific app, since it pulls templates from any/every app. Also, that's why dish_out_templates is in the root urls.py file.
        
def scheduleAllSports(request, year="None"): # generate information for all active sports in given year (eg Basketball, '2008-2009')
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct() 

    # create the list of variables for the template
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        # list of each sport's seasons in the given school year 
        sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))
    return render_to_response("scheduleAllSports.html", locals())

def scheduleOneSport(request, sportName, year="None"): # generate information for the specified sport in given school year
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct() 
    for s in sportList:
        s.lwr = s.Name.lower()

    # get the Sport object from the given sport name
    sportName = sportName.capitalize()
    sport = Sport.objects.get(Name=sportName)

    # list of this sport's seasons in the given school year 
    sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))

    return render_to_response("scheduleOneSport.html", locals())

def allSports(request, year="None"): # generate information for all active sports in given year (eg Basketball, '2008-2009')
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct() 

    # create the list of variables for the template
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        # list of each sport's seasons in the given school year 
        sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))
    return render_to_response("allSports.html", locals())

def oneSport(request, sportName, year="None"): # generate information for the specified sport in given school year
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct() 
    for s in sportList:
        s.lwr = s.Name.lower()

    # get the Sport object from the given sport name
    sportName = sportName.capitalize()
    sport = Sport.objects.get(Name=sportName)

    # list of this sport's seasons in the given school year 
    sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))

    return render_to_response("oneSport.html", locals())

def standingsAllSports(request, year="None"): # generate information for all active sports in given year (eg Basketball, '2008-2009')
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct() 

    # create the list of variables for the template
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        # list of each sport's seasons in the given school year 
        sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.divisionList = league.division_set.all()
                for division in league.divisionList:
                    division.teamList = division.team_set.all()
    return render_to_response("standingsAllSports.html", locals())

def standingsOneSport(request, sportName, year="None"): # generate information for the specified sport in given school year
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct() 
    for s in sportList:
        s.lwr = s.Name.lower()

    # get the Sport object from the given sport name
    sportName = sportName.capitalize()
    sport = Sport.objects.get(Name=sportName)

    # list of this sport's seasons in the given school year 
    sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))

    # create the list of variables for the template
    for season in sport.seasonList:
        season.leagueList = season.league_set.all()
        for league in season.leagueList:
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

def refereesAllSports(request, year="None"): # generate information for all the sports
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct() 

    # create the list of variables for the template
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        # list of each sport's seasons in the given school year 
        sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()
    return render_to_response("refereesAllSports.html", locals())
                    
def refereesOneSport(request, sportName, year="None"): # generate information for the specified sport
    if year=="None": # default to present school year
        today = datetime.today()
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
    else:
        intYear = int(year[0:3])
    yearStart = today.replace(year=intYear, month=7, day=1)
    yearEnd = yearStart.replace(year=intYear+1)

    # list of the sports with seasons in the given school year 
    sportList = Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct() 
    for s in sportList:
        s.lwr = s.Name.lower()

    # get the Sport object from the given sport name
    sportName = sportName.capitalize()
    sport = Sport.objects.get(Name=sportName)

    # list of this sport's seasons in the given school year 
    sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))

    # create the list of variables for the template
    for season in sport.seasonList:
        season.leagueList = season.league_set.all()
        for league in season.leagueList:
            league.refereeList = league.Referees.all()
    return render_to_response("refereesOneSport.html", locals())

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

def joinTeam(request):
    if request.method  == 'POST':
        form = RegisterTeamMember(request.POST)
        if form.is_valid():
                cd = form.cleaned_data
                teamMember = Person(StudentID=cd['schoolId'], FirstName=cd['FirstName'], LastName=cd['LastName'], ShirtSize="XXL", phoneNumber=cd['phoneNumber'])
                teamMember.save()
                
                return render_to_response("congrats.html", {"teammember":teamMember.FirstName, "teamname":team.Name,})

        else:
            return render_to_response("joinTeam.html", locals())

def createTeam1(request):
    if request.method  == 'POST':
        form = CreateTeamForm1(request.POST)
        if form.is_valid():
            #request.session['cd'] = form.cleaned_data
            UPAY_SITE_ID = 7
            return render_to_response("confirmPart1.html", locals())
        else:
            return render_to_response("createTeam1.html", locals())
    else:
        form = CreateTeamForm1()
        return render_to_response("createTeam1.html", {'form':form,})


def createTeam2(request):
    if request.method == 'POST':
        form = CreateTeamForm2(request.POST)
        if form.is_valid():
            if request.POST['teamPassword'] == request.POST["repeatTeamPassword"]:
                cd = request.session['cd']
                league = League.objects.get(id=cd['leagueId'])
                division = Division.objects.get(id=cd['leagueId'])
                captain = Person(StudentID=cd['captainId'], FirstName=cd['captainFirstName'], LastName=cd['captainLastName'], Email=cd['captainEmail'], ShirtSize="XXL", Address="236 W. Reade Ave.")
                team = Team(Name=cd['teamName'], Password=cd['teamPassword'], Captain=captain, Division = division, LivingUnit="Sammy II")
                team.save()
                captain.save()
            else:
                passwordError = True
                return render_to_response("createTeam2.html", locals())
    else:
        form = CreateTeamForm2()
        return render_to_response("createTeam2.html", {"passwordError":True, "form":form()})
