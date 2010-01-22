from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context
from django.core.urlresolvers import reverse
from datetime import datetime
from models import *
from forms import *
from django.core import serializers


def daySched(request):
    return HttpResponse("testing")

def getGames(request):
    if(not request.GET or request.GET['start'] == "" or request.GET['end'] == ""):
        return HttpResponse('"start" and "end" get values need to be passed')
    json_serializer = serializers.get_serializer("json")()
    o = Game.objects.select_related(depth=1).extra(where=["%s <= date(StartTime) and date(StartTime) <= %s"], params=[request.GET['start'], request.GET['end']])
    json_serializer.serialize(o, relations=('HomeTeam', 'AwayTeam',))
    val = json_serializer.getvalue()
    return HttpResponse(val);

