from django.template.defaultfilters import stringfilter
from django import template
register = template.Library()


def anchorWrap(val, href):
    return '<a href="%s">%s</a>' % (href, str(val))

def teamAnchorWrap(val, teamId):
    return anchorWrap(val, '/team/'+ str(teamId))

register.filter(anchorWrap)
register.filter(teamAnchorWrap)
