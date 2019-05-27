from django import template
from django.apps import apps
from datetime import datetime, timedelta
import pytz
import ast


register = template.Library()


@register.filter
def index(l, i):
    return l.index(i) + 1


@register.filter
def toList(string):
    return ast.literal_eval(string)


@register.filter
def justQs(l):
    q_list = []

    for qs in l:
        qs = qs[:-1]
        for q in qs:
            q_list.append(q)

    return q_list


@register.filter
def isActiveSession(created):
    time_threshold = created + timedelta(hours=2)
    now = datetime.now(pytz.timezone('Eire'))

    if now < time_threshold:
        return "Active Session"
    else:
        return "Completed Session"


@register.filter
def pullSession(sessionid):
    UserAnswer = apps.get_model('session_handler', 'UserAnswer')
    usersessiondata = UserAnswer.objects.filter(sessionid=str(sessionid)).order_by('-username')
    return usersessiondata
