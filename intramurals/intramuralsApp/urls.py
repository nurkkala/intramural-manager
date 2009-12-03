from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url('^$', 'index'),
    url('^sports/(.+)', 'oneSport'),# view info for a specific sport
    url('^sports$', 'allSports'),# view info for all sports
    url('^schedule/(.+)', 'scheduleOneSport'),# view schedule for a specific sport
    url('^schedule$', 'scheduleAllSports'),# view schedule for all sports
    url('^standings/(.+)', 'standingsOneSport'),# view standings for a specific sport
    url('^standings$', 'standingsAllSports'),# view standings for all sports
    url('^register', 'register'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam', 'joinTeam'),
    url('^referees/(\d+)', 'refereeSchedule'),# the schedule page for referee of given id
    url('^referees/(.+)', 'refereesOneSport'),# view referees for a specific sport
    url('^referees$', 'refereesAllSports'),# view referees for all sports
    url('^teams/(\d+)', 'teamHomepage'),# the home page for team of given id
    url('^about$', 'about'),
    url('^admin$', 'admin'),

)
