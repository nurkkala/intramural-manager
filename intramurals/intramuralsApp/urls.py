from django.conf.urls.defaults import *
urlpatterns = patterns('intramuralsApp.views',
    url('^mynameis/(.*)', 'say_hi'),
    url(r'^$', 'index'),
    url(r'^schedule$', 'schedule'),
    url('^sports$', 'sports'),
    url('^registerTeam', 'createTeam'),
    url('^standings$', 'standings'),
    url('^referees/(\d+)', 'refereeSchedule'),
    url('^referees$', 'referees'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(.*)', 'index'),
)
