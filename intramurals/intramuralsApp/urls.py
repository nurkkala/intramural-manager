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
    url('^teams/(\d+)', 'teamHomepage'),       # the home page for team of given id
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(sports|schedule|standings|referees)/([\w-]+)$', 'pageWithSport'),# sport specified
    url('^(sports|schedule|standings|referees)$', 'pageWithSport'),         # no sport specified

    url('^daySched','daySched'),
    url('^getGames', 'getGames'),

)
