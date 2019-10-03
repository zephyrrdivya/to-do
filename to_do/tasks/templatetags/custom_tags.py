from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def date_cal(value, arg):
    today = datetime.now()
    diff = (value - today).days

    h = 255*(((diff/2))/5)

    if diff < 0:
        return tuple([130, 130, 130])

    if diff > 0 and diff < 10:
        return tuple([255, h, h])

    return tuple([255, 255, 255])

    # return value.replace(arg, '')
