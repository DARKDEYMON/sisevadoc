from apps.evaluacion.setting_dinamic import initial_default_gestion, initial_default_periodo
from django import template

register = template.Library()

@register.simple_tag
def initial_default_gestion_tag():
	return initial_default_gestion()

@register.simple_tag
def initial_default_periodo_tag():
	return initial_default_periodo()

@register.simple_tag
def verbose_name_tag(obj, field_name):
	print(obj)
	return obj._meta.get_field(field_name).verbose_name