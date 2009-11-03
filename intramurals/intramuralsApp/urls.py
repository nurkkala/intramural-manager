from django.conf.urls.defaults import *
from intramuralsApp.views import index

urlpatterns = patterns('',
    url('^$', index),
    #url('', ),
)
