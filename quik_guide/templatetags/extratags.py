from datetime import date
from django import template

register = template.Library()

@register.simple_tag
def today(format = '%d %m %Y'):
    return str(date.today().strftime(format))
