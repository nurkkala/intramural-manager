from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from models import *
from django.db.models import Q
from forms import JoinTeamForm1, JoinTeamForm2
from django import forms
from django.core import serializers
from defaults import default
from templatetags.filters import *
from sandbox import *
from django.core.mail import send_mail
import re

PHONE_REGEX = r'^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})|\d{4,5}$'  
"""Description: Matches US phone number format. 1 in the beginning is optional, area code is required, spaces or dashes can be used as optional divider between number groups. Also alphanumeric format is allowed after area code. Also, accepts campust phone numbers of 4 or 5 digits
   Matches: 1-(123)-123-1234 | 123 123 1234 | 1-800-ALPHNUM | 85555
   Non-Matches: 1.123.123.1234 | (123)-1234-123 | 123-1234"""


def renderToResponse(template, params={}):
    UPAY_SITE_ID = 7
    EXT_TRANS_ID_LABEL = "This id is stored in Taylor's database to confirm that you have paid"

    sports = Sport.objects.all()
    d = {'static_pathname':'http://cse.taylor.edu/~cos372f0901/intramurals', 'sports':sports, 'URL_PREFIX':URL_PREFIX, 'UPAY_SITE_ID':UPAY_SITE_ID, 'EXT_TRANS_ID_LABEL':EXT_TRANS_ID_LABEL,}
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

def scheduleChooseSport(request):
    return renderToResponse('scheduleChooseSport.html',{'curSports':list(set([ol.Season.Sport for ol in OpenLeague.objects.all()])),})

def schedule(request, gameId=None, ):
    try:
        if not gameId:
            try:
                gameThisDay = Game.objects.filter(StartTime__gte=datetime.today())[0]
            except Exception as e:
                gameThisDay = Game.objects.latest("StartTime")
        else: # A day has been specified by passing the id of a game in that day
            gameThisDay = Game.objects.get(id=gameId)
        date = gameThisDay.StartTime

        try:
            prevGame = gameThisDay.get_previous_by_StartTime()
            while prevGame.StartTime.day == gameThisDay.StartTime.day:
                prevGame = prevGame.get_previous_by_StartTime()
        except Exception as e:
            prevGame = False        

        try:
            nextGame = gameThisDay.get_next_by_StartTime()
            while nextGame.StartTime.day == gameThisDay.StartTime.day:
                nextGame = nextGame.get_next_by_StartTime()
        except Exception as e:
            nextGame = False        

        gameList = Game.objects.filter(StartTime__year=(date.year)).filter(StartTime__month=(date.month)).filter(StartTime__day=(date.day))
        for game in gameList:
            game.r = Referee.objects.all()
    finally:
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


def validateTeamName(r):
    try:
        name = r.GET['Name']
        league_id = r.GET['League_id']
        division_id = Division.objects.get(League=league_id).id
    except Exception as e:
        return HttpResponse('')
    try:
        t = OpenTeam.objects.get(Name=name,Division=division_id)
        return HttpResponse('Sorry, that Team Name is already taken.')
    except Exception as e:
        return HttpResponse('')

def createTeam1(request, sportId):
    sport = Sport.objects.get(id=sportId)
    toa = gettoa(sport.Name)
    class CreateTeam1Form(forms.Form):
        leagues = OpenLeague.objects.filter(Season__Sport=sportId)
        leagueList = [ (l.id, l.Name) for l in leagues]
        sportList = [ (l.Season.Sport.id, l.Season.Sport.Name) for l in leagues]
        sportList = list(set(sportList)) #this is a hack way to remove duplicates from the sportList
        
        #sportId = forms.ChoiceField(sportList, label='sport: ', required = True)
        leagueId = forms.ChoiceField(leagueList, label='league: ', required = True)
        address = forms.ChoiceField(Person.FLOORS, label='Location on campus: ', required=True)
        teamName = forms.CharField(max_length=100, label=': ', required = True)
        #locationId = forms.CharField(max_length=50, label='Location on campus: ', required = True)
        captainFirstName = forms.CharField(max_length=50, label = 'Captain\'s First Name: ', required = True)
        captainLastName = forms.CharField(max_length=50, label = 'Captain\'s Last Name: ', required = True)
        captainGender = forms.ChoiceField(Person.GENDER, label='Gender: ', required=True)
        captainId = forms.IntegerField(label='Captain\'s school ID (without the @): ', required = True)
        captainEmail = forms.EmailField(label='Captain\'s email address: ', required = True)
        legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
        phoneNumber = forms.RegexField(PHONE_REGEX, label = 'Phone Number:', required=False)
        teamPassword = forms.CharField(max_length=50, label='Team Password: ', widget=forms.PasswordInput, required = True)
        repeatTeamPassword = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Repeat Team Password', required=True)
        emailList = forms.CharField(label = 'Please enter a list of e-mail addresses', required=False)
        uPaySiteId = forms.HiddenInput()
        shirtSize = forms.ChoiceField(list(Person.SHIRTSIZE), label = 'Shirt Size (we won\'t tell, promise)', required=True)

    if request.method  == 'POST':
        form = CreateTeam1Form(request.POST)
        if request.POST['teamPassword'] == request.POST["repeatTeamPassword"]:
            if form.is_valid():
                request.session['postPayDestination'] = "create"
                cd = form.cleaned_data
                captain =  Person(StudentID=cd['captainId'], FirstName=cd['captainFirstName'], LastName=cd['captainLastName'], Email=cd['captainEmail'], ShirtSize=cd['shirtSize'], Address="236 W. Reade Ave.", Gender=cd['captainGender'])
                division = Division.objects.get(League=cd['leagueId'])
                cd.update({
                       #'emailList': request.POST.getlist('inviteeEmailAddress'),
                        'captain': captain,
                        'team': Team(Name=cd['teamName'], Password=cd['teamPassword'], Captain=captain, Division = division, LivingUnit=cd['address']),
                        })
                try:
                    cd['team'].save()
                except Exception as e:
                    if re.search('key 3$',e[1]):
                        passTaken = 'That password will not work, please choose another'
                    if re.search('key 2$',e[1]):
                        teamNameTaken = 'That team name is already taken.'
                    error = True
                    return renderToResponse('createTeam1.html', locals())
                request.session['cd'] = cd
                BILL_NAME = cd['captainFirstName'] + ' ' + cd['captainLastName']
                return renderToResponse("confirmPart1.html", locals())
            
            else:
                error = True
                return renderToResponse("createTeam1.html", locals())
        else:
            error = True
            passwordsNoMatch = 'Your passwords must match.'
            return renderToResponse("createTeam1.html", locals())
    else:

        form = CreateTeam1Form()

        #existing_teams = OpenTeam.objects.all()
        return renderToResponse("createTeam1.html", locals())
            
def createTeam2(request):
    cd = request.session['cd']
    cd['captain'].save()
    cd['team'].Captain = cd['captain']
    cd['team'].save()
    message = "You have been invited by {0} {1}  to join their team called \"{2}\" this intramural season.  \n Please click the following link to join: http://taylorintramurals.net/joinTeam1?teamPassword={3}\n\nTeam Name: {2}\nTeam Password: {3}\nCaptain: {0} {1}\n\nThanks,\n-- Your Taylor Intramurals Crew".format(cd['captainFirstName'], cd['captainLastName'],cd['teamName'],cd['teamPassword'])
    emailList = filter(lambda _:_ != '', cd['emailList'])
    #if len(emailList) > 0:
        #send_mail('Intramurals Invitation', message, 'taylorintramurals@gmail.com', cd['emailList'], fail_silently=False)
    request.session['postPayDestination'] = False
    request.session['cd'] = False
    request.session['hasPaid'] = False
    return renderToResponse("congratsCreate.html", cd)

def paymentSuccess(request):
    request.session['haspaid'] = True
    try:
        if request.session['postPayDestination'] == "join":
            return joinTeam3(request)
        elif request.session['postPayDestination'] == "create":
            return createTeam2(request)
    except Exception as e:
        strerr =  '     type(e): ' + str(type(e))
        strerr += '      e.args: ' + str(e.args)
        strerr += '           e: ' + str(e)
        #strerr += '           e: ' + str(traceback.format_tb(sys.exc_info()))
        return HttpResponseRedirect('http://cse.taylor.edu/~cos372f0901/email_from_django.php?err_message='+strerr)

def joinTeam1(request, sportId):
    sport = Sport.objects.get(id=sportId)
    if request.method  == 'POST' or request.method  == 'GET' and request.GET.has_key('teamPassword'):
        if request.method  == 'POST':
            form = JoinTeamForm1(request.POST)
        if request.method  == 'GET':
            form = JoinTeamForm1(request.GET)
        form.is_valid()
        if isValidPassword(form.cleaned_data['teamPassword'],request):
            request.session['postPayDestination'] = "join"
            request.method = "FromJoinTeam1"
            return joinTeam2(request, sportId)
        else:
            return renderToResponse("joinTeam1.html", {'error':"Team not found with that password (it's case sensative)", 'form':form})
    else:
        form = JoinTeamForm1()
        return renderToResponse("joinTeam1.html", locals())
    
def isValidPassword(password,request):
    try:
        team = OpenTeam.objects.get(Password = password)
        request.session['team'] = team
        return True
    except Exception as e:
        return False
    
def joinTeam2(request, sportId):
    sport = Sport.objects.get(id=sportId)
    class JoinTeam2Form(forms.Form):
        FirstName = forms.CharField(max_length=40, label = 'First name:', required=True)
        LastName = forms.CharField(max_length=40, label = 'Last name:', required=True)
        gender = forms.ChoiceField(Person.GENDER, label='Gender: ', required=True)
        address = forms.ChoiceField(Person.FLOORS, label='Location on campus: ', required=True)
        Email = forms.EmailField(max_length=40, label = 'E-mail address:', required=True)
        shirtSize = forms.ChoiceField(list(Person.SHIRTSIZE), label = 'Shirt Size (we won\'t tell, promise)', required=True)
        phoneNumber = forms.RegexField(PHONE_REGEX, label = 'Phone Number:', required=False)
        schoolId = forms.IntegerField(label='school ID (without the @): ', required = True)
        toa = forms.CharField(initial=gettoa(sport), widget=forms.Textarea, label='')
        legal = forms.BooleanField(widget=forms.CheckboxInput, label='I agree :', required = True)
    team = request.session['team']
    if request.method  == 'POST':
        form = JoinTeam2Form(request.POST)
        if form.is_valid():
            request.session['cd'] = form.cleaned_data
            request.session['postPayDestination'] = 'join'
            return renderToResponse("confirmPart1.html", locals())
        else:
            return renderToResponse("joinTeam2.html", locals())
    else:
        form = JoinTeam2Form()
        return renderToResponse("joinTeam2.html", locals())
    
def joinTeam3(request):
    cd = request.session['cd']
    teamMember = Person(StudentID=cd['schoolId'], FirstName=cd['FirstName'], LastName=cd['LastName'], ShirtSize=cd['shirtSize'], PhoneNumber=cd['phoneNumber'], Email=cd['Email'], Gender=cd['gender'], Address=cd['address'])
    teamMember.save()
    team = request.session['team']
    TeamMember(Member = teamMember, Team_id = request.session['team'].id,PaymentStatus=1).save()
    sport = request.session['team'].Division.League.Season.Sport.Name
    return renderToResponse("congratsJoin.html", locals())

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

def home(req):
    return renderToResponse('home.html')

def noCCinstructions(request):
#    send_mail('Intramurals Invitation', message, 'taylorintramurals@gmail.com', cd['emailList'], fail_silently=False)
#    send_mail('Someone can not pay with a credit/debit card', 'Jan, Jeff, and Joe,\n\nThis is an automated message sent to you because someone said on our website that they cannot pay with creadit/debit card. They have been instructed to pay Jan King the money who will manually keep track of those who paid her.', 'taylorintramurals@gmail.com', 'taylorintramurals@gmail.com')
    return HttpResponse('yes')

def chooseSport(request):
    return renderToResponse('chooseSport.html', {'curSports':list(set([ol.Season.Sport for ol in OpenLeague.objects.all()])),})

def register(request, sportId):
    sport = Sport.objects.get(id=sportId)
    return renderToResponse('register.html', locals())

def gettoa(sport):
    return """

INTRAMURALS ACTIVITIES RELEASE 

WAIVER, RELEASE OF ANY AND ALL LIABILTY, AND INDEMNIFICATION IN CONNECTION WITH PARTICIPATION IN ATHLETIC ACTIVITIES 

TO BE READ AND SIGNED BY STUDENT AND/OR PARENTS PRIOR TO PARTICIPATION IN ANY INTRAMURALS ACTIVITY 
 

   For good and valuable consideration, including but not limited to inducing TAYLOR UNIVERSITY (.Taylor.) to permit the following described activity to be conducted on that portion of its premises specified by Taylor: INTRAMURAL %s (.Activity.), each of the Taylor students executing this document, desiring to participate in the Activity, hereby acknowledges and agrees that such participation is subject to and specifically conditioned upon the undersigned executing this document and agreeing to be legally bound by the following terms: 

      REPRESENTATIONS AND ACKNOWLEDGEMENTS 

I acknowledge and agree that:

1. Notwithstanding the efforts of Taylor with respect to my safety, my participation in the Activity may cause or result in injury to my person and/or my property, I, nevertheless, desire to participate in the Activity;

2. The undersigned.s participation in the Activity is not a part of the duties and responsibilities of the undersigned as a student or employee of Taylor nor anything incidental thereto;

3. The undersigned.s participation in the Activity is the voluntary act of the undersigned entered into solely for the enjoyment and benefit of the undersigned; and

4. The undersigned is not receiving any credit or compensation from Taylor for any of the time spent by the undersigned in preparing for or engaging in the Activity. 

RELEASES AND COVENANTS NOT TO SUE 

   The undersigned hereby releases and discharges Taylor, together with its successors, assigns, trustees, officers, employees, representatives, and agents, of and from any and all claims or liability of any type whatsoever, including but not limited to property damage, physical injury, mental anguish, embarrassment, defamation, and invasion of privacy, which the undersigned may suffer arising out of, based upon, resulting from, or in any way connected with the Activity or the undersigned.s participation therein, including but not limited to, any claim caused, or alleged to be caused, in whole or part, by sole, joint, several, or comparative negligence, breach of contract, breach of warranty, or other breach of duty by Taylor, or its successors, assigns, trustees, officers, employees, representatives or agents, or whether such claim, damage, or expense is asserted under a negligence, contract or warranty theory, a strict or other product liability theory, or any other legal theory.  The undersigned further agrees and covenants not to sue Taylor, its successors, assigns, trustees, officers, employees, representatives or agents, for any claim arising out of, based upon, resulting from, or in any way connected with the undersigned.s participation in the Activity. 

INDEMNIFICATION 

   The undersigned hereby agrees and covenants to defend, indemnify, and hold harmless Taylor, together with its successors, assigns, trustees, officers, employees, representatives and agents, and each of them, from and against all claims, damages, and expenses, including, but not limited to attorneys. fees and legal costs of defense, arising out of, based upon, resulting from, or in any way connected with or alleged to arise, be based upon, result from, or be in any way connected with the undersigned.s participation in the Activity, irrespective of whether or not such claim, damage or expense is caused or alleged to be caused, in whole or part, by the sole, joint, several, or comparative negligence, breach of contract, breach of warranty, or other breach of duty by Taylor, or its successors, assigns, trustees, officers, employees, representatives and agents, or whether such claim, damage or expense in asserted under negligence, contract or warranty theory, a strict or other product liability theory, or any other legal theory. 

SUMMARY 

   The undersigned hereby acknowledges and agrees that the undersigned understands that the foregoing releases, covenants not to sue, and indemnification mean that if the undersigned is injured or any property of the undersigned or any part thereof is damaged while the undersigned is participating in the Activity or going to or from the activity: 

   1. THE UNDERSIGNED WILL NOT BE ABLE TO RECOVER FROM TAYLOR FOR ANY SUCH INJURIES, LOSSES OR DAMAGES, EVEN IF SUCH INJURIES OR DAMAGES ARE DUE TO THE ACTS OR OMISSIONS OF TAYLOR, OR ITS SUCCESSORS, ASSIGNS, TRUSTEES, OFFICERS, EMPLOYEES, REPRESENTATIVES OR AGENTS; AND

 

   2. THE UNDERSIGNED WILL NOT BE ABLE TO MAKE A CLAIM OR FILE A LAWSUIT AGAINST TAYLOR OR ITS SUCCESSORS, ASSIGNS, TRUSTEES, OFFICERS, EMPLOYEES, REPRESENTATIVES OR AGENTS, EVEN THOUGH SUCH INJURIES, LOSSES OR DAMAGES ARE THE FAULT OF TAYLOR, ITS SUCCESSORS, ASSIGNS, TRUSTEES, OFFICERS, EMPLOYEES, REPRESENTATIVES, AND AGENTS.

""" % sport










