from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context
from django.core.urlresolvers import reverse
from datetime import datetime
from models import *
from forms import *
from django.core import serializers
import json

def index(request):
    return render_to_response("home.html")

#"dish_out_template" belongs in /intramurals/__init.py__  (or intramuals/views.py) because dish_out_template is logically independent of any specific app, since it pulls templates from any/every app. Also, that's why dish_out_templates is in the root urls.py file.
        
def yearStartOf(year): # get the start date of the school year given a string such as "2009-2010" ("None" defaults to present school year)
    today = datetime.today()
    if year==None: # default to present school year
        intYear = today.year
        if today.month < 7:            
            intYear = intYear-1
        return yearStartOf(str(intYear) + "-" + str(intYear+1))
    else:
        intYear = int(year[0:4])
    return today.replace(year=intYear, month=7, day=1)

def sportDropDownOf(sportName, yearSelected): 
    yearStart = yearStartOf(yearSelected)
    yearEnd = yearStart.replace(yearStart.year+1)
    if sportName==None:
        sportList =  Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct()
    else:
        sportList =  Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct()
    sportNameList = []
    for sport in sportList:
        sportNameList.append(sport.Name)
    return sportNameList
    
def sportListOf(sportName, yearSelected): # list of sports of which info is displayed (only one if viewing a specific sport)
    yearStart = yearStartOf(yearSelected)
    yearEnd = yearStart.replace(yearStart.year+1)
    if sportName==None:
        return Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct()
    else:
        return [Sport.objects.get(Name=sportName)]

def yearListOf(sportName, yearSelected): # generate a list of school years in which the particular sport has been played, starting with the given year
    yearList = [yearSelected]
    if sportName==None:
        seasonList = Season.objects.order_by('Start')
    else:
        sport = Sport.objects.get(Name=sportName)
        seasonList = sport.season_set.order_by('Start')
    for season in seasonList:
        year = season.Start.year
        if season.Start.month < 7:            
            year = year-1
        year = str(year) + "-" + str(year+1)
        if year not in yearList:
            yearList.append(year)
    return yearList

def seasonListOf(sport, yearSelected):
    yearStart = yearStartOf(yearSelected)
    yearEnd = yearStart.replace(yearStart.year+1)
    return sport.season_set.filter(Start__range=(yearStart, yearEnd))

def scheduleYearOnly(request, yearSelected): # generate information for all sports in given school year
    return schedule(request, None, yearSelected)

def schedule(request, sportName=None, yearSelected=None): # generate information for the specified sport in given school year
    # list of the sports that can be navigated to from this page (exclude a selected sport)
    sportDropDown = sportDropDownOf(sportName, yearSelected)

    # list of the sports being displayed (only one if viewing a specific sport)
    sportList = sportListOf(sportName, yearSelected)

    # list of years in which sports are played (or in which the selected sport is played)
    yearList = yearListOf(sportName, yearSelected)
 
    # create the list of variables for the template
    for sport in sportList:
        sport.seasonList = seasonListOf(sport, yearSelected)

    return render_to_response("base.html", locals())

def sportsYearOnly(request, yearSelected): # generate information for all sports in given school year
    return sports(request, None, yearSelected)

def sports(request, sportName=None, yearSelected=None): # generate information for all active sports in given year (eg Basketball, '2008-2009')
    # list of the sports that can be navigated to from this page (exclude a selected sport)
    sportDropDown = sportDropDownOf(sportName, yearSelected)

    # list of the sports being displayed (only one if viewing a specific sport)
    sportList = sportListOf(sportName, yearSelected)

    # list of years in which sports are played (or in which the selected sport is played)
    yearList = yearListOf(sportName, yearSelected)
 
    # create the list of variables for the template
    for sport in sportList:
        sport.seasonList = seasonListOf(sport, yearSelected)

    return render_to_response("base.html", locals())

def standingsYearOnly(request, yearSelected): # generate information for all sports in given school year
    return standings(request, None, yearSelected)

def standings(request, sportName=None, yearSelected=None): # generate information for all active sports in given year (eg Basketball, '2008-2009')
    # list of the sports that can be navigated to from this page (exclude a selected sport)
    sportDropDown = sportDropDownOf(sportName, yearSelected)

    # list of the sports being displayed (only one if viewing a specific sport)
    sportList = sportListOf(sportName, yearSelected)

    # list of years in which sports are played (or in which the selected sport is played)
    yearList = yearListOf(sportName, yearSelected)
 
    # create the list of variables for the template
    for sport in sportList:
        sport.lwr = sport.Name.lower()
        sport.seasonList = seasonListOf(sport, yearSelected)
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.divisionList = league.division_set.all()
                for division in league.divisionList:
                    division.teamList = division.team_set.all()

    return render_to_response("base.html", locals())

def record(team):
    homeWins = len(Game.objects.filter(HomeTeam__id=team.id).filter(Outcome=1)) # games won as home team
    awayWins = len(Game.objects.filter(AwayTeam__id=team.id).filter(Outcome=2)) # games won as away team
    homeLosses = len(Game.objpppects.filter(HomeTeam__id=team.id).filter(Outcome=2)) # games lost as home team
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

def refereesYearOnly(request, yearSelected): # generate information for all sports in given school year
    return referees(request, None, yearSelected)

def referees(request, sportName=None, yearSelected=None): # generate information for all the sports
    if request.is_ajax():
        sportName = request.GET.get("sportName")
        yearSelected = request.GET.get("yearSelected")
    # list of the sports that can be navigated to from this page (exclude a selected sport)
    sportDropDown = sportDropDownOf(sportName, yearSelected)

    # list of the sports being displayed (only one if viewing a specific sport)
    sportList = sportListOf(sportName, yearSelected)

    # list of years in which sports are played (or in which the selected sport is played)
    yearList = yearListOf(sportName, yearSelected)
 
    # create the list of variables for the template
    for sport in sportList:
        sport.seasonList = seasonListOf(sport, yearSelected)
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()

    template = "referees.html"
    data = {
        "sportName": sportName,
        "yearSelected": yearSelected,
        "sportList": sportList,
    }
    return render_to_response(template, data, RequestContext(request))

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

