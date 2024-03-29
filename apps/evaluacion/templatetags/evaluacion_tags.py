from apps.evaluacion.setting_dinamic import *#initial_default_gestion, initial_default_periodo, plan_mejorasa
from django import template

register = template.Library()

@register.simple_tag
def initial_default_gestion_tag():
	return initial_default_gestion()

@register.simple_tag
def initial_default_periodo_tag():
	return initial_default_periodo()

@register.simple_tag
def plan_mejoras_act():
	return 'Si '+str(initial_periodo_plnm()) +"/"+ str(initial_gestion_plnm()) if initial_plan_mejorasa() else 'No'

@register.simple_tag
def plan_mejoras_act_bool():
	return initial_plan_mejorasa()

@register.simple_tag
def create_user_active():
	return initial_crear_usuario()

@register.simple_tag
def verbose_name_tag(obj, field_name):
	#print(obj)
	return obj._meta.get_field(field_name).verbose_name

@register.simple_tag
def concat_string(value_1, value_2, value_3, value_4):
    return str(value_1) + str(value_2) + str(value_3) + str(value_4)

@register.filter
def replace_string(value):
	#print(value)
	return value.replace('Acción a la debilidad: ','')