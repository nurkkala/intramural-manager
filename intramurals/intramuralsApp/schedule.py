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
