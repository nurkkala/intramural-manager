from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from models import *
from django.db.models import Q
from forms import *
from django.core import serializers
from defaults import default
from templatetags.filters import *
import json
from sandbox import *

def renderToResponse(template, params={}):
    sports = Sport.objects.all()
    d = {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals', 'sports':sports, 'URL_PREFIX':URL_PREFIX}
    d.update(params)
#    return HttpResponse(d['static_pathname'])
    return render_to_response(template, d)

def index(request):
    return renderToResponse("base.html", {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals'})

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

def schedule(request, gameId=None):
    if not gameId:
        try:
            gameThisDay = Game.objects.filter(StartTime__gte=datetime.today())[0]
        except:
            gameThisDay = Game.objects.latest("StartTime")
    else: # A day has been specified by passing the id of a game in that day
        gameThisDay = Game.objects.get(id=gameId)
    date = gameThisDay.StartTime

    try:
        prevGame = gameThisDay.get_previous_by_StartTime()
        while prevGame.StartTime.day == gameThisDay.StartTime.day:
            prevGame = prevGame.get_previous_by_StartTime()
    except:
        prevGame = False        

    try:
        nextGame = gameThisDay.get_next_by_StartTime()
        while nextGame.StartTime.day == gameThisDay.StartTime.day:
            nextGame = nextGame.get_next_by_StartTime()
    except:
        nextGame = False        

    gameList = Game.objects.filter(StartTime__year=(date.year)).filter(StartTime__month=(date.month)).filter(StartTime__day=(date.day))
    for game in gameList:
        game.r = Referee.objects.all()

    return renderToResponse("schedule.html", locals())

def sports(request):
    # Note: Right now this displays all the sports seasons in the school year.
    # It should be modified to display only the sport(s) currently being played.
    yearSelected = thisYear()
    yearStart = yearStartOf(yearSelected)
    yearEnd = yearStart.replace(year=yearStart.year+1)

    seasonList = Season.objects.filter(Start__range=(yearStart, yearEnd)).distinct()
    static_pathname = 'http://cse.taylor.edu/~cos372f0901/intramurals'
    return renderToResponse("sports.html", locals())

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

    return renderToResponse(page + ".html", {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals'})

def teamHomePage(request, teamId):
    currentTeamRanking = TeamRanking.objects.get(Team=teamId)
    memberList = currentTeamRanking.Team.Members
    gameList = Game.objects.filter(
        Q(HomeTeam=teamId) | Q(AwayTeam=teamId)
        )
    teamRankingList = TeamRanking.objects.filter(Team__Division=currentTeamRanking.Team.Division)
    return renderToResponse("teamHomepage.html", locals())

def refereeSchedule(request, refId):
    referee = Referee.objects.get(id=refId)
    gameList = referee.game_set.all()
    for game in gameList:
        game.sport = teamToSport(game.HomeTeam.id)
    return renderToResponse("refereeSchedule.html", locals())


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
            return renderToResponse("confirmPart1.html", locals())
        else:
            return renderToResponse("createTeam1.html", locals())
    else:
        form = CreateTeamForm1()
        return renderToResponse("createTeam1.html", locals())

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
                team = Team(Name=cd['teamName'], Password=request.POST['teamPassword'], Captain=captain, Division = division, LivingUnit=cd['locationId'])
                team.save()
                return renderToResponse("congrats.html", {'teamname':cd['teamName'], 'teamcaptain':cd['captainFirstName'], 'teampassword':request.POST['teamPassword'],})
            else:
                passwordError = True
                return renderToResponse("createTeam2.html", locals())
        else:
            blank_form = CreateTeamForm2()
            return renderToResponse("createTeam2.html", {"form":blank_form,})
    else:
        form = CreateTeamForm2()
        return renderToResponse("createTeam2.html", {"passwordError":True, "form":form,})

def paymentSuccess(request):
    if request.session['destination'] == "join":
        return joinTeam2(request)
    elif request.session['destination'] == "create":
        return createTeam2(request)

#team = Team.objects.get(Password=request.POST["teamPassword"])
def joinTeam1(request):
    if request.method  == 'POST':
        form = JoinTeamForm1(request.POST)
        if form.is_valid()
            return renderToResponse("joinTeam2.html", locals())
        else:
            return renderToResponse("joinTeam1.html", {'error':"Team not found with that password (it's case sensative)", 'form':form})
    else:
        form = JoinTeamForm1()
        return renderToResponse("joinTeam1.html", locals())

def joinTeam2(request):
    if request.method  == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            teamMember = Person(StudentID=cd['schoolId'], FirstName=cd['FirstName'], LastName=cd['LastName'], ShirtSize="XXL", phoneNumber=cd['phoneNumber'])
            teamMember.save()
            return renderToResponse("congrats.html", {"teammember":teamMember.FirstName, "teamname":team.Name,})
        else:
            return renderToResponse("joinTeam2.html", locals())
    else:
        form = JoinTeamForm()
        return renderToResponse("joinTeam2", locals())

def standings(request):
    records = getCurrentLeaguesDivisionsTeams()
    return renderToResponse("standings.html", locals())

def defaults(req, command):
    if command=="":
        return renderToResponse('home.html')
    if (default[command]): #this is to whitelist what commands are allowed
        return renderToResponse(command + '.html')
    else:
        return HttpResponse("unknown page.")


def getCurrentLeaguesDivisionsTeams():
    """This function returns an object that has the current leagues, divisions for those leagues, and teams for those divisions """
    return [{'league':cl.League, 'divisions':[{'division':d, 'teams':[{'teamRanking':tr,} for tr in TeamRanking.objects.filter(Team__Division = d)]} for d in Division.objects.filter(League = cl.League)]} for cl in CurrentLeagues.objects.all()]
