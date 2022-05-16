from datetime import date
from django import template

register = template.Library()

@register.filter
def is_today(value):
    return value.date.date()