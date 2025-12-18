from django import template
from django.forms import BoundField


register = template.Library()


@register.filter
def klass(object):
    return object.__class__.__name__


@register.filter
def add_class(field, css_class):
    """Add CSS class to form field widget"""
    if not isinstance(field, BoundField):
        return field
    
    existing_class = field.field.widget.attrs.get('class', '')
    if existing_class:
        css_class = f"{existing_class} {css_class}"
        
    field.field.widget.attrs['class'] = css_class.strip()
    
    return field
    # return field.as_widget(attrs={'class': css_class.strip()})
