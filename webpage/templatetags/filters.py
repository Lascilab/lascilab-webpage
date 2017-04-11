from django import template
from random import shuffle

register = template.Library()

@register.filter(name='shuffle')
def shuff(a):
	if a:
		b = list(a)
		shuffle(b)
		return b
	return []
