from django.conf.urls.defaults import *
urlpatterns = patterns('intramuralsApp.views',
    url('^mynameis/(.*)', 'say_hi'),
    url('^$', 'index'),
    url('^referees/$', 'referees'),
    url('^(.*)', 'dish_out_template'),
)
