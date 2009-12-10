from django.conf.urls.defaults import *

urlpatterns = patterns('intramuralsApp.views',
    url('^getX$','getX'),# used for the json serializer (rename!)
    url('^$', 'index'),
    url('^sports/(\d{4}-\d{4})$', 'sportsYearOnly'),      # view info for all sports (year specified)
    url('^sports$', 'sportsYearOnly'),                    # view info for all sports (year specified)
    url('^sports/(.+)/(\d{4}-\d{4})$', 'sports'),         # view info for a specific sport (year specified)
    url('^sports/(.+)$', 'sports'),                       # view info for a specific sport (no year specified)
    url('^schedule/(\d{4}-\d{4})$', 'scheduleYearOnly'),  # view schedule for all sports (year specified)
    url('^schedule$', 'scheduleYearOnly'),                # view schedule for all sports (no year specified)
    url('^schedule/(.+)/(\d{4}-\d{4})$', 'schedule'),     # view schedule for a specific sport (year specified)
    url('^schedule/(.+)$', 'schedule'),                   # view schedule for a specific sport (no year specified)
    url('^teams/(\d+)', 'teamHomepage'),                  # the home page for team of given id
    url('^standings/(\d{4}-\d{4})$', 'standingsYearOnly'),# view standings for all sports (year specified)
    url('^standings$', 'standingsYearOnly'),              # view standings for all sports (no year specified)
    url('^standings/(.+)/(\d{4}-\d{4})$', 'standings'),   # view standings for a specific sport (year specified)
    url('^standings/(.+)$', 'standings'),                 # view standings for a specific sport (no year specified)
    url('^referees/(\d+)$', 'refereeSchedule'),           # the schedule page for referee of given id
    url('^referees/(\d{4}-\d{4})$', 'refereesYearOnly'),  # view referees for all sports (year specified)
    url('^referees$', 'refereesYearOnly'),                # view referees for all sports (year specified)
    url('^referees/(.+)/(\d{4}-\d{4})$', 'referees'),     # view referees for a specific sport (year specified)
    url('^referees/(.+)$', 'referees'),                   # view referees for a specific sport (year specified)
    url('^register', 'register'),
    url('^createTeam1', 'createTeam1'),
    url('^createTeam2', 'createTeam2'),
    url('^joinTeam1', 'joinTeam1'),
    url('^joinTeam2', 'joinTeam2'),
    url('^about$', 'about'),
    url('^admin$', 'admin'),
)
