from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^$','home'),
    url('^createTeam1/(\d+)', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1/(\d+)', 'joinTeam1'),
    url('^joinTeam2/(\d+)', 'joinTeam2'),
    url('^joinTeam3', 'joinTeam3'),
    url('^paymentSuccess', 'paymentSuccess'),
    url('^schedule$','schedule'),
    url('^schedule/(\d+)$','schedule'),# game id specified
    url('^standings','standings'),
    url('^(standings|referees)/([\w-]+)$', 'pageWithSport'),# sport specified
    url('^(standings|referees)$', 'pageWithSport'),         # no sport specified
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^team/(\d+)', 'teamHomePage'),       # the home page for team of given id

##    url('^about$', 'about'),  TODO: actually write this view. until then, don't uncomment or the admin/ functionality will break
##    url('^admin$', 'admin'),  TODO: actually write this view. until then, don't uncomment or the admin/ functionality will break

    url('^validateTeamName$', 'validateTeamName'),
    url('^noCCinstructions$', 'noCCinstructions'),
    url('^register/?$','chooseSport'),
    url('^register/(\d+)','register'),
    url('^(.*)$', 'defaults'),
)
