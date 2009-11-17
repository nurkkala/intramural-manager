from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url(r'^$', 'index'),
    url(r'^schedule$', 'schedule'),
    url('^sports$', 'sports'),
    url('^register', 'register'),
    url('^createTeam', 'createTeam'),
    url('^joinTeam', 'joinTeam'),
    url('^teams/(\d+)', 'teamHomepage'),# the home page for team of given id
    url('^standings/(.+)', 'standings'),# view standings for a specific sport
    url('^standings$', 'standings'),# view standings for all sports
    url('^referees/(\d+)', 'refereeSchedule'),# the schedule page for referee of given id
    url('^referees/(.+)', 'referees'),# view referees for a specific sport
    url('^referees$', 'referees'),# view referees for all sports
    url('^about$', 'about'),
    url('^admin$', 'admin'),
)
