from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url('^$', 'index'),
    url('^sports/(.+)/(\d.+)', 'sports'),# view info for a specific sport in specified year
    url('^sports/(\d.+)', 'sportsYearOnly'),# view info for all sports in specified year
    url('^sports/(.+)', 'sports'),# view info for a specific sport (no year specified)
    url('^sports$', 'sports'),# view info for all sports (no year specified)
    url('^schedule/(.+)/(\d.+)', 'schedule'),# view schedule for a specific sport in specified year
    url('^schedule/(\d.+)', 'scheduleYearOnly'),# view schedule for all sports in specified year
    url('^schedule/(.+)', 'schedule'),# view schedule for a specific sport (no year specified)
    url('^schedule$', 'schedule'),# view schedule for all sports (no year specified)
    url('^standings/(.+)/(\d.+)', 'standings'),# view standings for a specific sport in specified year
    url('^standings/(\d.+)', 'standingsYearOnly'),# view standings for all sports in specified year
    url('^standings/(.+)', 'standings'),# view standings for a specific sport (no year specified)
    url('^standings$', 'standings'),# view standings for all sports (no year specified)
    url('^register', 'register'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^referees/?(\d.+)?', 'refereesYearOnly'),# view referees for all sports in specified year
    url('^referees/(.+)/(\d.+)?/?(d)?', 'referees'),# view referees for a specific sport in specified year
    url('^teams/(\d+)', 'teamHomepage'),# the home page for team of given id
    url('^about$', 'about'),
    url('^admin$', 'admin'),
)
