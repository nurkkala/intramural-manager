from django.conf.urls.defaults import *
from intramurals import dish_out_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url('templates/(.*)', dish_out_template), #TODO: we need to make this secure (we can't allow .. directory)
    ('^css/(.*)','dish_out_css'),
    ('^js/(.*)','dish_out_js'),
    (r'^admin/(.*)', admin.site.root),
    (r'', include('intramurals.intramuralsApp.urls')),
        # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
