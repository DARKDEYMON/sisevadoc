from apps.evaluacion.setting_dinamic import initial_default
from django import template

register = template.Library()

@register.simple_tag
def initial_default_date():
	return initial_default()