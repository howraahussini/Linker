# This is a custom filters for template 

from django import template

register = template.Library()

@register.filter
def get_model_name(value):
    return value.__class__.__name__