from django.template.defaultfilters import stringfilter
from django import template
register = template.Library()


def anchorWrap(val, href):
    return '<a href="%s">%s</a>' % (href, val)

def teamAnchorWrap(val, teamId):
    return anchorWrap(val, '/team/'+teamId)

register.filter('anchorWrap',anchorWrap)
register.filter('teamAnchorWrap', teamAnchorWrap)
