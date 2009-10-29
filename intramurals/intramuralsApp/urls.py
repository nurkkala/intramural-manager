from django.conf.urls.defaults import *
from intramuralsApp.views import dish_out_template
urlpatterns = patterns('',
    url('^mynameis/(.*)', 'intramuralsApp.views.say_hi'),
    url('^$', 'intramuralsApp.views.index'),
    url('^(.*)', dish_out_template),
)
