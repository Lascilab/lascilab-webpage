from django import template
from random import shuffle

register = template.Library()

@register.filter(name='shuffle')
def shuff(a):
	return shuffle(list(a)) if a else []