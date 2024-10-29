   # core/templatetags/custom_filters.py
   
from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given argument."""
    if value is None:
        return []  # Return an empty list if value is None
    return value.split(arg)

@register.filter
def trim(value):
    """Trim whitespace from the beginning and end of a string."""
    if isinstance(value, str):
        return value.strip()
    return value

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
