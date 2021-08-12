from django import template
register  = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='times_dash') 
def times(number):
    return range(5-number)