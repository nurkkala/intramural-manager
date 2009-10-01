from django.conf.urls.defaults import *
from intramuralsApp.views import dish_out_template
urlpatterns = patterns('',
    url('^templates/(.*)', dish_out_template),
    url('^$', 'intramuralsApp.views.index'),
)
