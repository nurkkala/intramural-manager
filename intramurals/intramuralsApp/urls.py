from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^mynameis/(.*)', 'say_hi'),
    url('^getGames$','getGames'),
    url(r'^schedule$', 'schedule'),
    url('^sports$', 'sports'),
    url('^register', 'register'),
    url('^createTeam', 'createTeam'),
    url('^standings$', 'standings'),
    url('^referees/(\d+)', 'refereeSchedule'),
    url('^referees$', 'referees'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url(r'^$', 'index'),
    url('^email$', 'email'),
)
