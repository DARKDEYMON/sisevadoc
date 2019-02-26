from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(token_alumno)
admin.site.register(token_dcarrera)
admin.site.register(token_aevaluacion)
admin.site.register(cuestionario_alumno)
admin.site.register(cuestionario_aevaluacion)
admin.site.register(cuestionario_dcarrera)

class ItemEva(admin.ModelAdmin):
	#list_per_page = 5
	class Media:
		#css = {
		#    "screen": ("css/items/items.css",)
		#}
		js = ("/static/chainedfk.js",)

admin.site.register(evaluacion,ItemEva)
admin.site.register(comisiong)