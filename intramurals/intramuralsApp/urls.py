from django.conf.urls.defaults import *
from intramuralsApp.views import dish_out_template, index
urlpatterns = patterns('',
    url('^mynameis/(.*)', 'intramuralsApp.views.say_hi'),
    url('^$', index),
    url('^(.*)', dish_out_template),
)
