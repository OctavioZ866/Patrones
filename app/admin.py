from django.contrib import admin
from .models import Tejidos, Grafo


# Register your models here.
class TejidoAdmin(admin.ModelAdmin):
    list_display =('pk','partes', 'temperatura','color', 'inflamacion')
    list_filter =['temperatura','color', 'inflamacion']
    search_fields =['partes', 'temperatura','color', 'inflamacion']
    list_per_page = 10
admin.site.register(Tejidos,TejidoAdmin)

class GrafoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grafo,GrafoAdmin)
