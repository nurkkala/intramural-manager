from django.conf.urls.defaults import *
urlpatterns = patterns('intramuralsApp.views',
    url('^mynameis/(.*)', 'say_hi'),
    url('^$', 'index'),
    url('^schedule$', 'schedule'),
    url('^sports$', 'sports'),
    url('^register$', 'register'),
    url('^standings$', 'standings'),
    url('^referees$', 'referees'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
    url('^(.*)', 'dish_out_template'),
)
