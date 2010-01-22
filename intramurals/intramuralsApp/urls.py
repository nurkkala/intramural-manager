from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^$', 'index'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
    url('^joinTeam3', 'joinTeam3'),

    url('^(.*)$', 'defaults'),

    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^referees/?(.+)?/?(\d.+)?', 'referees'),# view referees for a specific sport in specified year
    url('^referees/(\d.+)', 'refereesYearOnly'),# view referees for all sports in specified year
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^teams/(\d+)', 'teamHomepage'),       # the home page for team of given id
    url('^teams/(\d+)', 'teamHomepage'),# the home page for team of given id
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(sports|schedule|standings|referees)/([\w-]+)/(\d{4}-\d{4})$', 'pageWithSport'),# view info for a specific sport (year specified)
    url('^(sports|schedule|standings|referees)/(\d{4}-\d{4})$', 'pageWithSportYearOnly'), # view info for all sports (year specified)
    url('^(sports|schedule|standings|referees)/([\w-]+)$', 'pageWithSport'),              # view info for a specific sport (no year specified)
    url('^(sports|schedule|standings|referees)$', 'pageWithSport'),                       # view info for all sports (no year specified)
)
