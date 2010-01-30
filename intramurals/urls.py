from django.conf.urls.defaults import *
from __init__ import dish_out_template

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url('templates/(.*)', dish_out_template), #TODO: delete this for production (security hole)
    (r'^admin/(.*)', include(admin.site.urls)),
#    (r'^admin/(.*)', admin.site.root),
    (r'', include('intramuralsApp.urls')),
    (r'', include('jcal.urls')),
)
