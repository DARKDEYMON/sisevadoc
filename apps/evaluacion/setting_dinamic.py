from constance import config
import datetime

def initial_active_gestion():
	return config.GESTION_ACTIVO

def initial_gestion():
	return config.GESTION

def initial_periodo():
	return config.PERIODO

def initial_default_gestion():
	return config.GESTION if initial_active_gestion() else datetime.datetime.now().year

def initial_default_periodo():
	return config.PERIODO if initial_active_gestion() else ( 1 if datetime.datetime.now().month<=6 else 2)

def initial_gestion_plnm():
	return config.GESTION_PLNM

def initial_periodo_plnm():
	return config.PERIODO_PLNM

def initial_plan_mejorasa():
	return config.PLN_MEJORA

def initial_crear_usuario():
	return config.CREAR_USER