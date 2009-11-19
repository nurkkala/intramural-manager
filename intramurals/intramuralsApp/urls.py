from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^mynameis/(.*)', 'say_hi'),
    url('^getX$','getX'),
    url(r'^$', 'index'),
    url(r'^schedule$', 'schedule'),
    url('^sports$', 'sports'),
    url('^register', 'register'),
    url('^createTeam', 'createTeam'),
    url('^joinTeam', 'joinTeam'),
    url('^teams/(\d+)', 'teamHomepage'),
    url('^standings/(.+)', 'standings'),
    url('^standings$', 'standings'),
    url('^referees/(\d+)', 'refereeSchedule'),
    url('^referees$', 'referees'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
)
