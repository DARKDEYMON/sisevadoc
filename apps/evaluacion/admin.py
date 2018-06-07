from django.contrib import admin
from .models import *

# Register your models here.

class ItemEva(admin.ModelAdmin):
	#list_per_page = 5
	class Media:
		#css = {
		#    "screen": ("css/items/items.css",)
		#}
		js = ("/static/chainedfk.js",)

admin.site.register(evaluacion,ItemEva)