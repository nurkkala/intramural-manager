# Create your views here.
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from models import *

def index(request):
    return render_to_response("home.html")

def say_hi(request, name):
    t = Template("<html><body>Well hi there {{ name_of_person }}!</body></html>")
    c = Context({'name_of_person': name})
    html = t.render(c)
    return HttpResponse(html)

def dish_out_template(request, file_name):
    return render_to_response(file_name)
	
def referees(request):
    sportList = Sport.objects.all()
    for sport in sportList:
        sport.seasonList = sport.season_set.all()
        for season in sport.seasonList:
            season.leagueList = season.league_set.all()
            for league in season.leagueList:
                league.refereeList = league.Referees.all()
    return render_to_response("referees.html", locals())
