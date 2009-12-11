from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url('^$', 'index'),
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^teams/(\d+)', 'teamHomepage'),       # the home page for team of given id
    url('^register', 'register'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
	url('^joinTeam3', 'joinTeam3'),
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^referees/(.+)/(\d.+)', 'refereesOneSport'),# view referees for a specific sport in specified year
    url('^referees/(\d.+)', 'refereesAllSports'),# view referees for all sports in specified year
    url('^referees/(.+)', 'refereesOneSport'),# view referees for a specific sport (no year specified)
    url('^referees$', 'refereesAllSports'),# view referees for all sports (no year specified)
    url('^teams/(\d+)', 'teamHomepage'),# the home page for team of given id
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(.+)/(\d{4}-\d{4})$', 'pageYearOnly'),# view info for all sports (year specified)
    url('^(.+)$', 'pageYearOnly'),              # view info for all sports (year specified)
    url('^(.+)/(.+)/(\d{4}-\d{4})$', 'page'),   # view info for a specific sport (year specified)
    url('^(.+)/(.+)$', 'page'),                 # view info for a specific sport (no year specified)
)
