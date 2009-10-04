from django.conf.urls.defaults import *
from intramuralsApp.views import dish_out_template, index

urlpatterns = patterns('',
    url('^templates/(.*)', dish_out_template),
    url('^$', index),
)
