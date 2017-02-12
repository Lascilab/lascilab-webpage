from django import template
from random import shuffle

register = template.Library()

@register.filter(name='shuffle')
def shuff(a):
    a = list(a)
    shuffle(a)
    return a