from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^$','schedule'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
    url('^paymentSuccess', 'paymentSuccess'),
##    url('^joinTeam3', 'joinTeam3'),  TODO: actually write this view. until then, don't uncomment or the admin/ functionality will break
    url('^schedule$','schedule'),
    url('^schedule/(.+)$','schedule'),# game id specified
    url('^standings','standings'),
    url('^(standings|referees)/([\w-]+)$', 'pageWithSport'),# sport specified
    url('^(standings|referees)$', 'pageWithSport'),         # no sport specified
    url('^referees/(\d+)$', 'refereeSchedule'),# the schedule page for referee of given id
    url('^team/(\d+)', 'teamHomePage'),       # the home page for team of given id
##    url('^about$', 'about'),  TODO: actually write this view. until then, don't uncomment or the admin/ functionality will break
##    url('^admin$', 'admin'),  TODO: actually write this view. until then, don't uncomment or the admin/ functionality will break

    url('^(.*)$', 'defaults'),
)
