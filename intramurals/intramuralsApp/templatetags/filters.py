from django.template.defaultfilters import stringfilter
from django import template
register = template.Library()


def anchorWrap(val, href):
    return '<a href="%s">%s</a>' % (href, val)
anchorWrap.is_safe = True

def teamAnchorWrap(val, teamId):
    return anchorWrap(val, '/team/'+teamId)
teamAnchorWrap.is_safe = True


register.filter(anchorWrap)
register.filter(teamAnchorWrap)
