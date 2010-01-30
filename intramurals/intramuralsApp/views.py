from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context
from django.core.urlresolvers import reverse
from datetime import datetime
from models import *
from forms import *
from django.core import serializers
from defaults import default
from schedule import *
import json

def index(request):
    return render_to_response("base.html", {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals'})

def thisYear(): # return this school year in proper format (eg "2009-2010")
    today = datetime.today()
    intYear = today.year
    if today.month < 7:            
        intYear = intYear-1
    return str(intYear) + "-" + str(intYear+1)

def yearStartOf(year): # get the start date of the school year given a string such as "2009-2010"
    today = datetime.today()
    intYear = int(year[0:4])
    return today.replace(year=intYear, month=7, day=1)

def yearListOf(sportName, yearSelected): # list of school years in which the particular sport has been played, starting with the given year
    yearList = [yearSelected]
    seasonList = Season.objects.order_by('Start')
    for season in seasonList:
        year = season.Start.year
        if season.Start.month < 7:            
            year = year-1
        year = str(year) + "-" + str(year+1)
        if year not in yearList:
            yearList.append(year)
    return yearList

def daySched(request, specifiedDate=None):
    date = datetime.today()
    if not specifiedDate:
        gameThisDay = Game.objects.latest("StartTime")
        date = gameThisDay.StartTime
    else:
        m = int(specifiedDate[0:2])
        d = int(specifiedDate[2:4])
        y = int(specifiedDate[4:8])
        date.replace(year=y, month=m, day=d)
        sameYear = Game.objects.filter(StartTime__year=(date.year))
        sameMonth = sameYear.filter(StartTime__month=(date.month))
        sameDay = sameMonth.filter(StartTime__day=(date.day))
        gameThisDay = sameDay.latest("StartTime")

    try:
        prevGame = gameThisDay.get_previous_by_StartTime()
        while prevGame.StartTime.day == gameThisDay.StartTime.day:
            prevGame = prevGame.get_previous_by_StartTime()
    except:
        prevGame = False        

    try:
        nextGame = gameThisDay.get_next_by_StartTime()
        while nextGame.StartTime.day == gameThisDay.StartTime.day:
            nextGame = prevGame.get_next_by_StartTime()
    except:
        nextGame = False        

    gameList = Game.objects.filter(StartTime__year=(date.year)).filter(StartTime__month=(date.month)).filter(StartTime__day=(date.day))
    if request.is_ajax():
        return render_to_response("scheduleContent.html", locals())
    else:
        return render_to_response("schedule.html", locals())

def pageWithSport(request, page, sportName="current"): # generate information for the specified sport
    yearSelected = thisYear()
    yearStart = yearStartOf(yearSelected)
    yearEnd = yearStart.replace(yearStart.year+1)
    today = datetime.today()
    

    if sportName == "current":
        currentSports = True
    else:
        sportName = sportName.capitalize()
    sportList = Sport.objects.filter(season__Start__range=(yearStart, yearEnd)).distinct()
    sportDDList =  Sport.objects.exclude(Name=sportName).filter(season__Start__range=(yearStart, yearEnd)).distinct()

    sportDropDown = []
    for sport in sportDDList:
        sportDropDown.append(sport.Name)

    for sport in sportList:
        sport.seasonList = sport.season_set.filter(Start__range=(yearStart, yearEnd))
        for season in sport.seasonList:
            season.gameList = Game.objects.filter(HomeTeam__Division__League__Season=season.id).distinct().order_by("-StartTime")
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()
                league.divisionList = league.division_set.all()
                for division in league.divisionList:
                    division.teamList = division.team_set.all()
                    for team in division.teamList:
                        team.record = record(team)

    return render_to_response(page + ".html", {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals'})

def teamHomepage(request, teamId):
    team = Team.objects.get(id=teamId)
    team.record = record(team)
    opponentList = team.Division.team_set.all()
    memberList = team.Members.all()
    for opponent in opponentList:
        opponent.record = record(opponent)
    return render_to_response("teamHomepage.html", locals())

def refereeSchedule(request, refId):
    referee = Referee.objects.get(id=refId)
    gameList = referee.game_set.all()
    for game in gameList:
        game.sport = teamToSport(game.HomeTeam.id)
    return render_to_response("refereeSchedule.html", locals())

def record(team):
    homeWins = len(Game.objects.filter(HomeTeam=team).filter(Outcome=1)) # games won as home team
    awayWins = len(Game.objects.filter(AwayTeam=team).filter(Outcome=2)) # games won as away team
    homeLosses = len(Game.objects.filter(HomeTeam=team).filter(Outcome=2)) # games lost as home team
    awayLosses = len(Game.objects.filter(AwayTeam=team).filter(Outcome=1)) # games lost as away team
    homeTies = len(Game.objects.filter(HomeTeam=team).filter(Outcome=3)) # games tied as home team
    awayTies = len(Game.objects.filter(AwayTeam=team).filter(Outcome=3)) # games tied as away team
    wins = homeWins + awayWins
    losses = homeLosses + awayLosses
    ties = homeTies + awayTies
    record = str(wins) + "-" + str(losses)
    if ties > 0:
        record = record + "-" + str(ties)
    return record

def teamToSport(teamId):
    team = Team.objects.get(id=teamId)
    sport = team.Division.League.Season.Sport
    return sport
    
def createTeam1(request):
    if request.method  == 'POST':
        form = CreateTeamForm1(request.POST)
        if form.is_valid():
            request.session['cd'] = form.cleaned_data
            UPAY_SITE_ID = 7
            BILL_NAME = request.session['cd']['captainFirstName']
            EXT_TRANS_ID_LABEL = "This id is stored in Taylor's database to confirm that you have paid"
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
                captain.save()
                team = Team(Name=cd['teamName'], Password=request.POST['teamPassword'], Captain=captain, Division = division, LivingUnit="Sammy II")
                team.save()
                return render_to_response("congrats.html", {'teamname':cd['teamName'], 'teamcaptain':cd['captainFirstName'], 'teampassword':request.POST['teamPassword'],})
            else:
                passwordError = True
                return render_to_response("createTeam2.html", locals())
        else:
            blank_form = CreateTeamForm2()
            return render_to_response("createTeam2.html", {"form":blank_form,})
    else:
        form = CreateTeamForm2()
        return render_to_response("createTeam2.html", {"passwordError":True, "form":form,})

def joinTeam1(request):
    if request.method  == 'POST':
        form = JoinTeamForm1(request.POST)
        if request.POST["teampassword"]:
            team = Team.objects.get(Password=request.POST["teampassword"]) 
            return
        else:
            return render_to_response("joinTeam.html", locals())
    else:
        form = JoinTeamForm()
        return render_to_response("joinTeam1.html", locals())

def joinTeam2(request):
    if request.method  == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            teamMember = Person(StudentID=cd['schoolId'], FirstName=cd['FirstName'], LastName=cd['LastName'], ShirtSize="XXL", phoneNumber=cd['phoneNumber'])
            teamMember.save()
            return render_to_response("congrats.html", {"teammember":teamMember.FirstName, "teamname":team.Name,})
        else:
            return render_to_response("joinTeam2.html", locals())
    else:
        form = JoinTeamForm()
        return render_to_response("joinTeam2", locals())

def defaults(req, command):
    if (default[command]): #this is to whitelist what commands are allowed
        return render_to_response(command + '.html', {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals'})
    else:
        return HttpResponse("unknown page.")
