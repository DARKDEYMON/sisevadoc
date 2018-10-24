from constance import config
import datetime

def initial_active_gestion():
	return config.GESTION_ACTIVO

def initial_gestion():
	return config.GESTION

def initial_default():
	return config.GESTION if initial_active_gestion() else datetime.datetime.now().year
