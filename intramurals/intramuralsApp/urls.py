from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url('^$', 'index'),
    url('^sports/(.+)/(\d.+)', 'oneSport'),# view info for a specific sport in specified year
    url('^sports/(\d.+)', 'allSports'),# view info for all sports in specified year
    url('^sports/(.+)', 'oneSport'),# view info for a specific sport (no year specified)
    url('^sports$', 'allSports'),# view info for all sports (no year specified)
    url('^schedule/(.+)/(\d.+)', 'scheduleOneSport'),# view schedule for a specific sport in specified year
    url('^schedule/(\d.+)', 'scheduleAllSports'),# view schedule for all sports in specified year
    url('^schedule/(.+)', 'scheduleOneSport'),# view schedule for a specific sport (no year specified)
    url('^schedule$', 'scheduleAllSports'),# view schedule for all sports (no year specified)
    url('^standings/(.+)/(\d.+)', 'standingsOneSport'),# view standings for a specific sport in specified year
    url('^standings/(\d.+)', 'standingsAllSports'),# view standings for all sports in specified year
    url('^standings/(.+)', 'standingsOneSport'),# view standings for a specific sport (no year specified)
    url('^standings$', 'standingsAllSports'),# view standings for all sports (no year specified)
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^teams/(\d+)', 'teamHomepage'),       # the home page for team of given id
    url('^register', 'register'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(.+)/(.+)/(\d{4}-\d{4})$', 'pageWithSport'),# view info for a specific sport (year specified)
    url('^(.+)/(\d{4}-\d{4})$', 'pageWithSportYearOnly'),  # view info for all sports (year specified)
    url('^(.+)/(.+)$', 'pageWithSport'),              # view info for a specific sport (no year specified)
    url('^(.+)$', 'pageWithSport'),                   # view info for all sports (no year specified)
)
