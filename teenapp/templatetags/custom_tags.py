from django import template
from teenapp.models import Teen
 
register = template.Library()

@register.filter
def remainder(value, arg):
    return value % arg